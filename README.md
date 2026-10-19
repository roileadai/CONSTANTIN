# CONSTANTIN — The Constant Agent

> **Always on. Never forgets. Verifiable.** — Инфраструктура для соло-разработчика 2026: память, скиллы и безопасный рантайм для AI-агентов на своих VPS.

**Стек соло-фабрики 2026:** `Coolify / Dokploy` + `OpenClaw 300k★ / Hermes 247k★` + `n8n 207k★` + `Telegram Stars` + `Next.js + Supabase` → **1 VPS €15/мес заменяет $80k payroll**

---

## 📂 Что внутри этого репо

| Файл | Что это | Когда читать |
|---|---|---|
| [`RESEARCH_2026-10-19.md`](RESEARCH_2026-10-19.md) | Глубокий аудит аккаунта `roileadai` + бренд CONSTANTIN + рынок 19.10.2026 + 7 гипотез-проектов | Старт здесь |
| [`RESEARCH_MARKETS_AI_TELEGRAM_SAAS_2026-10-20.md`](RESEARCH_MARKETS_AI_TELEGRAM_SAAS_2026-10-20.md) | Рынки AIFirst / TelegramFirst / SaaSFirst + каталог 40+ бесплатных GitHub-репо (MIT/Apache2) + почасовая хронология 10ч → 100ч → масштаб | Выбор MVP |
| [`ROADMAP_90_DAYS.md`](ROADMAP_90_DAYS.md) | Канбан-доска 90 дней: Foundation → Memory → Notion OS → Skills → PMF | Ежедневный трекер |
| [`infra/`](infra/) | Готовые `docker-compose.yml` + `.env.example` для VPS-фабрики 24/7 (Coolify-альтернатива + raw Docker) | Деплой за 30 мин |
| [`mvp/telegram-ai-bot/`](mvp/telegram-ai-bot/) | Скелет MVP #1: Telegram AI-бот на `aiogram` 5.9k★ с Stars-платежами, памятью и n8n-хуками | `3-6ч до первых $` |
| [`docs/DELEGATION.md`](docs/DELEGATION.md) | Модель делегации: что делает человек (5-10ч/нед) vs AI-агенты на VPS (168ч/нед) | Операционка |

---

## 🚀 Быстрый старт (10 часов до первого $)

```bash
# 1. VPS Hetzner CPX32 €15/мес (2vCPU/4GB) + домен constantin.sh
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
# → получаешь Heroku на своем сервере: 280+ one-click, auto-SSL, Postgres 1-click

# 2. Клонируй MVP #1 (самый быстрый)
git clone https://github.com/roileadai/CONSTANTIN && cd CONSTANTIN/mvp/telegram-ai-bot
cp .env.example .env # вставь BOT_TOKEN от @BotFather + OPENAI_API_KEY
docker compose up -d  # 30 сек → бот live

# 3. Или Mini App (TS)
npx @telegram-apps/create-mini-app@latest
# шаблон: Telegram-Mini-Apps/nextjs-template 370★ + tma.js 1.2k★

# 4. Или SaaS (Cron Monitor, доказанный $14k MRR)
git clone https://github.com/ixartz/SaaS-Boilerplate && cd SaaS-Boilerplate
# MIT, Clerk+Drizzle+Stripe, 12.9k★ — добавь 1 таблицу checks
```

**Через 10ч твоего времени (AI отработает 80-120ч параллельно):** живой бот/Mini App со Stars-платежом, логами и мониторингом. Первые 10 юзеров, 1-2 платежа (1000 Stars = ~$13 net).

---

## 🧠 8 MVP по приоритету (от быстрого к долгому)

| # | MVP | Стек (бесплатно) | Срок | Цена | MRR потолок |
|---|---|---|---|---|---|
| **1** | **Telegram AI-Concierge** | `aiogram` 5.9k★ + `AstrBot` 41.9k★ + `n8n` 207k★ | 3-6ч | 300 Stars | $5-15k |
| **2** | **Mini App Utility** | `tma.js` 1.2k★ + `nextjs-template` 370★ | 6-10ч | 500 Stars + subs | $5-15k |
| **3** | **Cron/Uptime SaaS** | `ixartz` 12.9k★ MIT | 8-12ч | $9-19/мес | $14k+ |
| **4** | **API Changelog SaaS** | `Open SaaS` 15.7k★ MIT | 12-16ч | $19-49/мес | $5-12k |
| **5** | **Vertical AI Bot** | `LangBot` 15.4k★ + `Rasa` 21k★ | 12-20ч | $39-99/мес | $10-30k |
| **6** | **Content Repurposer** | `awesome-n8n-templates` 280+ | 6-10ч | $15-49/мес | $2-5k |
| **7** | **Skill Pack → ClawHub** | `openclaw/skills` + `awesome-skills` 52.9k★ | 4-8ч/skill | $29/мес | $5-25k |
| **8** | **Agency Stack** | `self-hosted-ai-kit` 15.3k★ | 10-15ч | $2k/клиент | $10-50k |

Все репо MIT/Apache2, кроме `midday` AGPL (используй как референс).

---

## 🏗️ VPS-фабрика 24/7 — Архитектура на 1-2 VPS

```
[VPS-1: €15/мес, 2vCPU/4GB/NVMe] — твой штаб
 ├─ Coolify (61k★) — Heroku на своем сервере
 │  ├─ n8n:5678 — оркестрация 24/7 (Telegram trigger, cron, webhook)
 │  ├─ Postgres + Redis (1-click)
 │  ├─ OpenClaw Gateway:18789 / Hermes:3000 — твой AI-оператор (код, ревью, саппорт 24/7)
 │  ├─ Next.js SaaS/Mini App:3000 — продукт
 │  └─ Uptime Kuma + Grafana — мониторинг
 └─ GitHub → Coolify auto-deploy (git push = deploy)

[VPS-2: €12/мес, 1vCPU/2GB] — опционально, приватный LLM
 └─ Hermes Agent + Ollama — без API-платежей, для приватных данных
```

**Делегация:**
- **Ты (5-10ч/нед):** ниша, цена, промпты `SOUL.md` — решения, которые меняют деньги
- **AI (168ч/нед):** кодит (Claude Code), тестит (Probe), отвечает юзерам (AstrBot), генерит контент (Beacon), деплоит (Coolify)

**Стоимость:** Minimal €12 (бот) → Standard €28 (бот+MiniApp+SaaS) → Full €84 (3+ агента). Заменяет $80-120k payroll — 50x leverage.

---

## ⏱️ Почасовая хронология

### 10ч твоего времени (AI 80-120ч параллельно) → живой продукт + первые $

| Ты | AI на VPS | Результат |
|---|---|---|
| 0-1ч: ниша + `constantin.sh` + BotFather token | idle | домен + токен |
| 1-2ч: VPS + Coolify (1 команда) | генерит `AGENTS.md` | инфраструктура как Heroku |
| 2-4ч: пишешь `PROMPT.md`, `git push` | Claude Code пишет бота, коммитит каждые 30 мин | первый деплой live |
| 4-6ч: Stars платежи (300 Stars = $3.9 net), тест | n8n webhook → Postgres → receipt | платеж работает |
| 6-8ч: пост в 3 TG-канала, 5 DM, affiliate 7% | отвечает 24/7, логирует | 10 юзеров, 1-2 платежа |
| 8-10ч: 3 бага → обновляешь `PROMPT.md` | чинит (Trace/Forge), деплоит v0.2 | v0.2 live |

### 100ч (недели 2-6) → $500-2k MRR, 100-500 юзеров

15ч/нед твоего ревью + 600-800ч AI: 1 фича/нед, weekly subscription, 1 PH launch, второй SaaS на том же VPS. Портфель как у Pieter Levels ($3M/год, 0 сотрудников).

### 100ч+ (5-10ч/нед) → $5-50k MRR, портфель

1 skill/мес на ClawHub (31k skills) + 1 micro-SaaS/6 нед → 5-10 продуктов × $1-5k = $10-30k MRR. Или outcome-агентство $2k/клиент, 60-80% маржа. Exit 2-4x ARR.

---

## 💰 Telegram Stars — экономика 2026

| Факт | Значение |
|---|---|
| 1 Star net тебе | ~$0.013 (1000 Stars = $13 via Fragment в TON, 21 день холд) |
| Desktop без Apple 30% | $0.013, mobile $0.009 — пушь desktop-оплату |
| Weekly подписки | 55.5% revenue (vs 43% в 2024), конверт 5.4x vs annual |
| Hybrid модель | 60-70% rewarded ads + 30-40% IAP + Stars subs |
| Обязателен | Digital goods внутри TG = только Stars (правило Telegram) |

---

## 📊 Рынок для соло 2026

- **36.3%** новых стартапов — соло (было 23.7% в 2019), 63% Stripe Atlas — соло
- Micro-SaaS **$15.7B→$59.6B к 2030**, AI-native растет 30-50%/год
- Base44: 1 чел, 6 мес → **$80M exit Wix**. Medvi: 1 чел → **$401M revenue** → $1.8B трек
- **Claude Code #1** (39% global), 90% девов на AI-агентах weekly

---

## 🗂️ Структура репо

```
CONSTANTIN/
├─ README.md                                    # ты здесь
├─ RESEARCH_2026-10-19.md                       # аудит + 7 гипотез
├─ RESEARCH_MARKETS_AI_TELEGRAM_SAAS_2026-10-20.md  # рынки + 40+ реп + хронология
├─ ROADMAP_90_DAYS.md                           # канбан 90 дней
├─ infra/
│  ├─ docker-compose.yml                        # VPS-фабрика (n8n+PG+Redis+OpenClaw)
│  ├─ docker-compose.minimal.yml                # $12 VPS, 1 бот
│  └─ .env.example                              # шаблон секретов
├─ mvp/
│  └─ telegram-ai-bot/                          # скелет MVP #1 (aiogram)
│     ├─ bot.py
│     ├─ .env.example
│     ├─ requirements.txt
│     └─ README.md
├─ docs/
│  └─ DELEGATION.md                             # модель делегации
└─ .github/
   └─ workflows/ci.yml                           # CI для проверки
```

---

## 📜 Лицензия и моат

- Код MVP — **MIT** (делай что хочешь)
- Доки/исследования — **CC BY 4.0**
- Moat соло 2026: не код (его пишут AI), а **аудитория + ниша + distribution** в Telegram/GitHub

> **Правило 2026:** Ship every 14 days. No perfection. 1 твой час = 10 часов AI. Так строят $80M соло.

---

## 🔗 Быстрые ссылки

- `infra/docker-compose.yml` → подними фабрику за 30 мин
- `mvp/telegram-ai-bot/` → задеплой бота за 10 мин
- Issues → задай вопрос, AI-агент ответит
- Discussions → предложи новую нишу

*Срез 20.10.2026, MAX mode, верифицировано gh api + search depth 3. Рынок меняется weekly — пересматривай гипотезы каждые 14 дней.*
