# MVP #1 — Telegram AI-Concierge Bot

**Стек:** `aiogram` 5.9k★ MIT (Python async) — де-факто для production AI-ботов 2026

**Время:** 3-6ч до первых $ (Stars)

## Запуск локально
```bash
pip install -r requirements.txt
cp .env.example .env # вставь BOT_TOKEN + OPENAI_API_KEY
python bot.py
```

## Деплой на VPS (1 команда)
```bash
# из infra/
docker compose --env-file .env -f docker-compose.minimal.yml up -d
docker logs -f mvp-telegram-ai-bot
```

## Stars-оплата
- BotFather → твой бот → `Edit Bot → Payments` → включи Stars
- Цена: 150 Stars Signal (~$1.95 net), 750 Stars Pro (~$9.75) — 1000 Stars = $13 net
- Webhook успешной оплаты → Postgres → n8n дайджест тебе в TG

## Куда дальше
- Подключи `AstrBot` 41.9k★ для памяти 24/7
- Добавь `n8n self-hosted AI kit` (Ollama) — без OpenAI $$
- Клонируй в Mini App: `npx @telegram-apps/create-mini-app` (тот же бэкенд)

См. `RESEARCH_MARKETS_AI_TELEGRAM_SAAS_2026-10-20.md` §4 #1
