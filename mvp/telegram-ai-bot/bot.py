"""
CONSTANTIN — MVP #1: Telegram AI-Concierge Bot (aiogram 5.9k★ MIT)
3-6ч до первых $ — Stars-платежи, память в Postgres, n8n-хук

Установка:
  pip install -r requirements.txt
  cp .env.example .env  # вставь BOT_TOKEN + OPENAI_API_KEY
  python bot.py          # polling (для VPS) или webhook (см. infra/)

Stars-цены: 150 Stars/мес Signal (~$1.95 net), 750 Stars Pro (~$9.75) — 1000 Stars = $13 net
"""
import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import LabeledPrice, PreCheckoutQuery

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Упрощенная память: в проде замени на Postgres + pgvector (см. infra/)
memory: dict[int, list] = {}

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN) if BOT_TOKEN else None
dp = Dispatcher()

@dp.message(Command("start"))
async def start(m: types.Message):
    await m.answer(
        "👋 CONSTANTIN — твой постоянный AI в Telegram\n\n"
        "Команды:\n"
        "/ask <вопрос> — спроси AI (Claude/GPT)\n"
        "/img <промпт> — сгенерить картинку\n"
        "/buy — купить Pro за Stars (750⭐ = ~$9.75 net)\n"
        "/status — твой тариф и лимиты\n\n"
        "Платишь Stars (внутри TG), вывод через Fragment, 21 день холд."
    )

@dp.message(Command("ask"))
async def ask(m: types.Message):
    q = m.text.removeprefix("/ask").strip() or "Привет!"
    # TODO: подключи OpenAI/Anthropic: client.chat.completions.create(...)
    # MVP-заглушка: эхо + делегация на n8n webhook (aiogram → n8n → LLM → TG)
    await m.answer(f"🤖 AI ответ на: {q}\n\n(подключи OPENAI_API_KEY в .env — сейчас заглушка)")

@dp.message(Command("buy"))
async def buy(m: types.Message):
    # Stars-платеж: 750 Stars = Pro (цена 77 Stars/$1 → ~$9.75 net)
    # Док: https://core.telegram.org/bots/api#sendinvoice — currency XTR (Stars)
    prices = [LabeledPrice(label="CONSTANTIN Pro (30 дней)", amount=750)]
    await bot.send_invoice(
        chat_id=m.chat.id,
        title="CONSTANTIN Pro",
        description="Безлимит AI, память, приоритет",
        payload="pro_30d",
        currency="XTR",
        prices=prices,
    )

@dp.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(q.id, ok=True)

@dp.message(F.successful_payment)
async def success(m: types.Message):
    await m.answer("✅ Оплата Stars получена! Pro активирован на 30 дней.\nСпасибо — ты поддержал соло-фабрику 24/7.")
    # TODO: запиши в Postgres: user_id, payload, stars, ts
    # TODO: триггер n8n webhook: новый платящий → дайджест в твой TG

@dp.message(Command("status"))
async def status(m: types.Message):
    await m.answer("Тариф: Free (100 запросов/мес)\nКупи /buy для Pro.")

async def main():
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN не задан — создай бота у @BotFather и заполни .env")
        return
    logging.info("CONSTANTIN bot polling started…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
