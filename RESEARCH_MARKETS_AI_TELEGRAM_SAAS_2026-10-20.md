# РЫНКИ ДЛЯ СОЛО-РАЗРАБОТЧИКА 2026: AIFirst • TelegramFirst • SaaSFirst + ДЕЛЕГАЦИЯ НА AI-АГЕНТОВ НА VPS

> **Срез:** 20.10.2026 • Режим MAX • Фокус: максимум делегирования на AI-агентов на арендованных VPS • Источники: GitHub API + web-search depth 2-3
> **Для кого:** соло-разработчик с 0-10ч/нед своего времени, готовый арендовать 1-2 VPS по €12-28/мес и отдать 80% работы агентам 24/7

---

## 0. TL;DR — Что делать в ближайшие 10 часов

1. **Арендуй 1 VPS Hetzner CPX32 / Contabo VPS S (2 vCPU, 4GB, NVMe, ~€15/мес) + домен `constantin.sh`**
2. **Поставь Coolify (61k★, Apache2) или Dokploy (37k★) — 30 мин, получаешь Heroku на своем сервере**
3. **Залей 1 из 3 самых быстрых MVP (выбирай по скиллам):**
   - **#1 Telegram AI-бот на Stars (3-6ч до первых $)** → `aiogram` 5.9k★ / `grammY` 3.8k★ + `n8n self-hosted AI kit` 15.3k★
   - **#2 Telegram Mini App Utility (6-10ч)** → `Telegram-Mini-Apps/nextjs-template` 370★ + `tma.js` 1.2k★
   - **#3 Cron/Uptime SaaS (8-12ч)** → `ixartz/SaaS-Boilerplate` 12.9k★ (MIT) или `midday` 8k★ (AGPL, клон готового SaaS) + `healthchecks.io` логика
4. **Запусти AI-агентов на том же VPS:** `OpenClaw` 300k★ (Gateway) или `Hermes Agent` 247k★ ($5 VPS, 1vCPU/2GB) — они будут кодить, тестить, отвечать юзерам пока ты спишь
5. **Подключи оплату:** Telegram Stars (1000 Stars = ~$13 net тебе, вывод через Fragment в TON, 21 день холд) + Stripe через Coolify одним кликом

**Через 10ч твоего времени (AI отработают ~80-120ч параллельно) у тебя должен быть живой бот/Mini App со Stars-платежом и логированием.**

---

## 1. КАРТА РЫНКОВ — Где деньги соло в 2026

### 1.1 Методология оценки
Оцениваем по 5 осям для соло: `Скорость до $` × `Делегация AI` × `Distribution friction` × `MRR потолок` × `Moat`

| Рынок | Суть 2026 | Размер / Динамика | Distribution | Монетизация | Оценка соло |
|---|---|---|---|---|---|
| **AIFirst** | AI-агент делает работу вместо софта. `Agents become the customer` — 20+ компаний уже с live agent-payments (Cloudflare x402) [1]. 90% девов юзают AI-агентов weekly, Claude Code #1 (39% global) [2] | AI agent market $5.25B→$7.84B→$52.6B к 2030 [3]. Микро-SaaS $15.7B→$59.6B к 2030 [4] | GitHub, X, HN, ClawHub (31k+ skills) | Usage $9-49/мес, outcome $500-2k/клиент | ⭐⭐⭐⭐⭐ |
| **TelegramFirst** | 950M+ MAU, боты = значимый трафик [5]. 500M+ юзеров Mini Apps/мес [6]. Stars — единственная валюта для digital goods внутри Telegram | Пик 1.44B MAU Mini Apps (Sep 2024) → 150-190M mid-2025 [7]. Catizen $35M+ с 55M игроков [8] | Инстант: ссылка на бота, нет App Store review | Stars: 1 Star≈$0.013 net тебе (1000 Stars=$13), desktop без 30% Apple. Подписки 30д, weekly 55.5% revenue [9] | ⭐⭐⭐⭐⭐ |
| **SaaSFirst** | Вертикальные микро-SaaS: 1 фича × 1 ниша × 1 канал продаж. Healthchecks $14k MRR соло part-time [10], Churnkey $30k+ MRR, Bannerbear $60k MRR соло | Медиана micro-SaaS $136 MRR [11], топ соло $5-50k MRR за 12-18 мес. 40% bootstrapped SaaS < $1M растут 14%/год, AI-native 30-50% [12] | SEO, Reddit/IndieHackers, Stripe App Store, Product Hunt | $9-99/мес, 80-90% маржа | ⭐⭐⭐⭐ |
| **API/DevToolFirst** | Dev платит за снятие боли: localhost tunnel, cron, API changelog | Ngrok/Neon/PlanetScale — доказали. Лояльность высока, churn низкий | GitHub, HN, Dev.to | $5-20/мес, dev-бюджеты | ⭐⭐⭐ |
| **ExtensionFirst** | Chrome/Telegram/Notion-плагин = distribution внутри платформы | Closet Tools $200k ARR соло [3], но риск бана платформы | Chrome Web Store, Notion Marketplace | $19-49 one-time + $9/мес | ⭐⭐⭐ |
| **ContentFirst** | AI генерирует контент, человек продает исход | Submagic $8M/год на 13 чел [13], Photo AI $130k MRR соло | X/LinkedIn/TikTok | $19-49/мес + агентство | ⭐⭐⭐ |

### 1.2 Почему именно AIFirst + TelegramFirst + SaaSFirst — твой стек
- **AIFirst = мозг** (OpenClaw/Hermes + n8n на VPS 24/7)
- **TelegramFirst = distribution** (0 friction, Stars-платежи, viral)
- **SaaSFirst = деньги** (рекуррент, 80% маржа, выход 2-4x ARR)

> **Solo-экономика 2026:** 36.3% новых стартапов — соло (было 23.7% в 2019) [14], 63% Stripe Atlas Q2'26 — соло [15]. Стек $300-500/мес заменяет $80-120k payroll [16]. 38% 7-figure бизнесов — соло с AI [17]. Base44 — соло за 6 мес → $80M exit Wix [18]. Medvi — 1 чел, $401M revenue, трек на $1.8B [19].

---

## 2. КАТАЛОГ БЕСПЛАТНЫХ GITHUB-РЕПО — Что брать в работу (все MIT/Apache2, кроме помеченных)

### 2.1 TelegramFirst — Фреймворки и Mini Apps

| Репо | Звезд | Язык | Лицензия | Что закрывает | Когда брать |
|---|---|---|---|---|---|
| **python-telegram-bot** | 29.5k | Python | LGPL-3.0 | Самый популярный Python-обертка Bot API, async, 3.11+, job queue | Python-стек, нужен rich API |
| **aiogram** | 5.9k | Python | MIT | Modern async, FSM, middleware, webhook+polling. Де-факто для production AI-ботов [5] | **DEFAULT для AI-ботов Python** |
| **telegraf** | 9.2k | TS/Node | MIT | Express-подобный middleware, Bot API 7.1, форум-топики, reactions | Node/TS стек |
| **grammY** | 3.8k | TS | MIT | TS-first, plugin ecosystem, Deno, отличные типы. Растет быстрее telegraf | **DEFAULT для TS** |
| **go-telegram/bot** | 1.9k | Go | MIT | Zero-dependency, Bot API 10.3 (Aug 2026) | Go, нужен минимальный оверхед на VPS |
| **tucnak/telebot** | 4.6k | Go | MIT | Чистый API, inline mode | Go альтернатива |
| **teloxide** | 4.2k | Rust | MIT/Apache | Elegant Rust framework | Rust-бот |
| **LangBot (ex-QChatGPT)** | 15.4k | Python | MIT | 10+ IM платформ: TG+Discord+Slack+QQ+WeChat+LINE+Lark → LLM [20] | Мультиплатформа одним ботом |
| **AstrBot** | 41.9k | Python | MIT | AI Agent Assistant, IM+LLMs+plugins+MCP, openclaw alternative | **AI-агент в Telegram из коробки** |
| **Botpress** | 14.5k | TS | MIT | Visual flow builder, NLU, Telegram/Slack/Teams | Enterprise visual |
| **Rasa** | 21k | Python | Apache2 | Самый продвинутый NLU, battle-tested | Сложный NLU |
| **Flowise** | 49k | TS | Apache2 | Drag-n-drop LangChain flows, acquired Workday 2025 | Low-code LLM chains |
| **Telegram-Mini-Apps/tma.js** | 1.2k | TS | MIT | Официальный SDK Telegram Mini Apps, все пакеты | **Обязателен для Mini App** |
| **Telegram-Mini-Apps/nextjs-template** | 370 | TS | MIT | Next.js+TS+TON Connect+tma.js, готовый шаблон | **Старт Mini App за 10 мин** |
| **Buidlso/telegram-mini-app-nextjs** | — | TS | MIT | Next.js+shadcn+tailwind+@tma.js/sdk | Mini App с красивым UI |
| **telegram-mini-apps-dev/vanilla-js** | 212 | HTML | MIT | Минимал без build tools, GitHub Pages deploy | Прототип за 1ч |
| **telegram-mini-apps-dev/vite-boilerplate** | 200 | TS | MIT | React+TS+Vite+HMR+ESLint | Vite Mini App |
| **goldpulpy/tma-backend-boilerplate** | — | Python | MIT | FastAPI+SQLAlchemy+DDD, backend для Mini App | Python backend Mini App |
| **nikandr-surkov/Hamster-Kombat-Clone** | — | TS | MIT | Next.js+React+TS, tap-to-earn, все ассеты | Клон игры за выходные |
| **awesome-telegram-bots** | — | — | CC0 | Курированный список всех фреймворков/Mini Apps | Ресерч |
| **awesome-telegram-ai-bots** | — | — | CC0 | Production AI-боты, LLM, voice, payments, memory (обновлен 2026-04-18) [5] | Ресерч AI-ботов |

### 2.2 AIFirst — Агенты, n8n, Skills

| Репо | Звезд | Лицензия | Что закрывает | VPS требование |
|---|---|---|---|---|
| **n8n-io/n8n** | 207k | Sustainable Use | Workflow automation, AI Agent nodes, Telegram/Slack trigger | 2GB (4GB rec), Docker |
| **n8n-io/self-hosted-ai-starter-kit** | 15.3k | Apache2 | Docker Compose: n8n+Ollama+Qdrant+Postgres → локальные AI-workflows за 5 мин | 4GB+ если Ollama, иначе 2GB |
| **enescingoz/awesome-n8n-templates** | — | MIT(файлы) | 280+ готовых workflows: Gmail, Telegram, Slack, Discord, Sheets, AI agents, RAG | Импорт 1 кликом |
| **coleam00/local-ai-packaged** | — | MIT | Ollama+Supabase+n8n+Open WebUI+SearXNG в одном compose | All-in-one локальный AI |
| **myname173/agent-platform** | — | MIT | 8 контейнеров, 24 n8n workflows, LobeHub chat+Next.js console+Telegram+MCP в одном хосте (смоке 71/71) [21] | 1 VPS, `docker compose up -d` |
| **keelstamphq/n8n-templates** | — | MIT | Per-client spend cap, approval via Wait link, hash-chained log — для агентств | n8n |
| **openclaw/openclaw** | 300k+ | MIT | Personal AI assistant, Telegram/Discord/Slack, gateway на твоем сервере, 50+ интеграций | 2vCPU/4GB (8GB с browser) [22] |
| **nousresearch/Hermes Agent** | 247k | MIT | Autonomous agent с persistent memory, learning loop, $5 VPS (1vCPU/2GB) [23] | **Самый дешевый агент** |
| **VoltAgent/awesome-openclaw-skills** | 52.9k | MIT | 5,400+ skills из ClawHub (13k+ всего), фильтр по категориям [24] | OpenClaw |
| **openclaw/clawhub** | 9.4k | MIT | Официальный skill registry, как npm для агентов, векторный поиск | OpenClaw |
| **openclaw/agent-skills** | — | MIT | 40+ built-in skills + beam/crabbox/handoff | OpenClaw |
| **agency-agents (obra)** | 157k | MIT | Виртуальные personas (Shell), живут в твоем coding tool, не хостятся | 0 RAM, твой Claude Code |
| **LangGraph / CrewAI / AutoGen** | 14k/25k/38k | MIT | State graph / Role crew / Conversational | Python |
| **Hermes Agent $5 guide** | — | — | Гайд деплоя на $5 VPS, Docker, API key LLM [25] | Contabo/Hetzner $5 |

### 2.3 SaaSFirst — Boilerplates (только свободные MIT)

| Репо | Звезд | Лицензия | Стек | Что внутри |
|---|---|---|---|---|
| **vercel/nextjs/saas-starter** | 16k | MIT | Next.js+Postgres+Drizzle+Stripe+shadcn | Официальный минимал, production-ready |
| **ixartz/SaaS-Boilerplate** | 12.9k | MIT | Next.js 16+TS+Tailwind4+Clerk+Drizzle+Stripe+Resend+Sentry | Лучший бесплатный full-stack, Pro $99 |
| **Wasp/Open SaaS** | 15.7k | MIT | Wasp+React+Prisma+Stripe+Polar+S3+shadcn | Самый полный free, admin+jobs+uploads |
| **T3 Stack** | 28.9k | MIT | Next.js+tRPC+Prisma+Auth.js+Tailwind | Type-safe фундамент, CLI |
| **Taxonomy** | 19.2k | MIT | Next.js+Contentlayer+Prisma+Auth.js+Stripe | Контент-heavy SaaS, блог/MDX |
| **midday-ai/midday** | 8k | AGPL-3.0 ⚠️ | Next15+TS+Supabase+Drizzle+Turborepo+Trigger.dev+Tinybird+Expo | **Реальный SaaS клон** (€→ $MRR бизнес), нельзя закрыть исходники |

> ⚠️ AGPL-3.0 = если модифицируешь и даешь доступ по сети — обязан открыть код. Для SaaS-бизнеса — риск. Используй как референс архитектуры, не как закрой-код-стартер.

### 2.4 VPS / Deploy — Своя PaaS за €15/мес

| Репо | Звезд | Лицензия | Min VPS | Idle RAM | Фишка 2026 |
|---|---|---|---|---|---|
| **coollabsio/coolify** | 61k | Apache2 | 2GB/2CPU/30GB | ~800MB | 280+ one-click, MCP server, Ollama first-class, Traefik auto-SSL, Git deploy [26] |
| **Dokploy** | 37k | Apache2* | 2GB/30GB | ~600MB | Docker Swarm, 500+ templates, легче Coolify [27] |
| **Dokku** | 32k | MIT | 1GB | ~50-100MB | Heroku `git push`, самый легкий, CLI |
| **CapRover** | 15k | Apache2 | 2GB | ~500MB | Swarm-native, stable |
| *Dokploy core Apache2 + DSAL carve-out на resale |

**Выбор:** Solo + 1 VPS + много apps → **Coolify** (если RAM ≥4GB) или **Dokploy** (если ≤2GB). Нужен минимум → **Dokku**.

---

## 3. ИНФРАСТРУКТУРА ДЕЛЕГАЦИИ — Твоя фабрика 24/7 на VPS

### 3.1 Архитектура на 1-2 VPS (€28-56/мес)

```
[VPS-1: Hetzner CPX32 €15/мес] — 2 vCPU / 4GB / 80GB NVMe / Ubuntu 24.04
  └─ Coolify (пайплайн)
     ├─ n8n (5678) — оркестрация всех workflows (24/7)
     │   ├─ Telegram trigger (бот)
     │   ├─ Cron (daily digest, backup)
     │   └─ Webhook (Mini App, SaaS, GitHub)
     ├─ Postgres + Redis (1-click в Coolify)
     ├─ OpenClaw Gateway (18789) или Hermes Agent (3000) — твой личный AI-оператор
     │   └─ Умеет: код (Claude Code), ревью (Lens 162 агента [28]), доки (Scribe), тесты (Probe)
     ├─ Next.js SaaS / Mini App (3000) — твой продукт
     └─ Uptime Kuma + Grafana (мониторинг 24/7)

[VPS-2 опционально €12/мес, 1vCPU/2GB] — Hermes Agent + Ollama (локальные LLM без API-платежей)
  └─ Для приватных данных / оффлайн-инференса
```

### 3.2 Модель делегации — Кто что делает

| Задача | Ты (человек, €100/ч) | AI-агент на VPS (24/7, €0.5/ч) |
|---|---|---|
| **Идея, ниша, цена** | 100% — ты решаешь, кого и почем | 0% — не делегируй стратегию |
| **Код MVP** | 10% — пишешь промпт `AGENTS.md`, ревьюишь PR | 90% — Claude Code пишет код, OpenHands тестит, Forge чинит билды [28] |
| **Дизайн** | 5% — выбираешь из 280+ one-click Coolify apps | 95% — Lovable/v0 генерит лендинг, агента |
| **Контент/SEO** | 10% — 1 пост/нед в X | 90% — Beacon-агент генерит блог, проверяет GSC, публикует [28] |
| **Поддержка** | 0% | 100% — AstrBot/Botpress отвечает в Telegram 24/7, escalate только сложное |
| **Деплой/инфра** | 5% — `git push` | 95% — Coolify auto-build, auto-SSL, backup |
| **Продажи** | 20% — 1 демо-звонок/день | 80% — n8n триггерит DMs, скилл `aladdn-market` продает на ClawMarket [24] |

**Правило:** Твое время = только решения, которые меняют деньги. Остальное = `SKILL.md` + `SOUL.md` для агента.

### 3.3 Стоимость делегации

| Конфиг | VPS | AI API | Итого/мес | Заменяет |
|---|---|---|---|---|
| **Minimal** (1 бот) | €12 (Virtua 1vCPU/2GB) [22] | $20 (Claude Haiku) | ~€35 | Фрилансер $1k |
| **Standard** (бот+Mini App+SaaS) | €28 (2vCPU/4GB) | $50-100 | ~€80 | Команда $5k |
| **Full factory** (3+ агента, DB, browser) | €84 (6vCPU/12GB) [22] | $150-250 | ~€250 | Стартап $20k |

> OpenClaw full stack $300-500/мес заменяет $80-120k payroll [16] — 50x leverage.

---

## 4. РЕЙТИНГ MVP — От самого быстрого к долгому (все с бесплатными репами)

### #1 — Telegram AI-Concierge Bot (TelegramFirst + AIFirst) — 3-6ч до первых $

**Боль:** Люди хотят AI без подписки $20/мес, прямо в Telegram. Боты с AI — топ-3 distribution для conversational AI в 2026 [5].
**Аудитория:** 950M Telegram, 41.9k★ AstrBot доказал: люди платят Stars за AI-ответы.
**Продукт:** Бот: `/ask` → ответ Claude/GPT, `/img` → DALL-E/FLUX, `/transcribe` → Whisper, `/memory` → помнит чат (как aiogram+SQLAlchemy+SQLite [29]).
**Монетизация:** Stars: 150 Stars/мес Signal (~$1.95 net), 750 Stars Pro (~$9.75) [30]. 10k платящих × 100 Stars = ~$9k/мес net [31]. Weekly подписки конвертят 5.4x лучше annual [9].
**Стек + репы:**
- `aiogram` 5.9k★ MIT + `python-telegram-bot` 29.5k★ + `telegram-search` 4.1k★
- `herval/cliobot` — готовый open-source genAI bot (DALL·E+Whisper+GPT-4) [32]
- `myname173/agent-platform` — 24 n8n workflows с Telegram-бриджом
- `n8n self-hosted AI kit` — Ollama локально, без OpenAI $

**Делегация:**
- Ты 2ч: выбрать нишу (напр. "AI для Etsy-продавцов в TG"), промпт SOUL.md, цена 300 Stars
- AI 24/7: пишет бота (Claude Code), тестит (Probe), отвечает юзерам (AstrBot), ведет табличку (Google Sheets)

---

### #2 — Telegram Mini App Utility — AI Credit Pack / Subscription — 6-10ч

**Боль:** 500M юзеров Mini Apps/мес [6], но 90% покупок — Day 0 [9]. Нужна утилита с instant value.
**Идеи (выбери 1):** 
- *AI Thumbnail Maker* (как Pikzels $25k MRR) — загрузил фото → 5 превью
- *Invoice/Quote Generator* (как Mini-Woo + Stripe [33]) — для фрилансеров, 2 клика
- *Habit Tracker + AI Coach* — daily nudge в Telegram

**Монетизация:** Stars покупки (digital goods) + Stars subscriptions (30д, tiered) [34] + rewarded ads (мини-апп сети, $0.35-0.50 CPM [9]). Hybrid: 60-70% ads + 30-40% IAP [9].
**Стек + репы:**
- `Telegram-Mini-Apps/nextjs-template` 370★ + `tma.js` 1.2k★ + `TelegramUI` React
- `Buidlso/nextjs-boilerplate` (shadcn) или `vite-boilerplate` (React+TS)
- `Hamster-Kombat-Clone` — вся механика tap-to-earn бери оттуда
- `goldpulpy/tma-backend-boilerplate` (FastAPI+Postgres) для бэка

**Делегация:** Агент генерит UI (Figma→code), n8n шлет пуши, Coolify деплоит на Pages (GitHub Pages бесплатно).

---

### #3 — Micro SaaS: Cron/Uptime Monitor (SaaSFirst) — 8-12ч до $1k MRR

**Боль:** Самый доказанный solo-SaaS: Healthchecks.io 652 клиента × $14k MRR part-time, 1 dev [10]. Разработчики редко уходят с монитора, который уже работает.
**Продукт:** Проще чем Cronitor: добавь URL → пинг каждые 1 мин → Telegram alert если down. Плати $9/мес за 50 мониторов.
**Монетизация:** $9-19/мес, $100/мес infra, маржа 95%. Exit 2-4x ARR.
**Стек + репы:**
- `ixartz/SaaS-Boilerplate` 12.9k★ MIT (free, Clerk+Drizzle+Stripe) → клонируешь, добавляешь 1 таблицу `checks`
- `vercel/saas-starter` 16k★ MIT — еще проще
- `Uptime Kuma` (open-source, self-host) — форкни логику пинга, не пиши с нуля
- `Coolify` — Postgres 1-click, cron job внутри n8n

**Делегация:** Агент пишет пинг-воркер, n8n шлет алерты, OpenClaw skill `probe` тестит API 24/7.

---

### #4 — API Changelog / Docs SaaS (API-First) — 12-16ч

**Боль:** API-команды платят $99+/мес ReadMe за доки, но changelog — отдельная боль.
**Продукт:** Подключи GitHub → AI генерит changelog из коммитов → публикует `/changelog` + Telegram-дайджест.
**Монетизация:** $19-49/мес, таргет $5-12k MRR [35]
**Стек + репы:** `ixartz` + `Open SaaS` + `agency-agents/Log` (auto-changelog from git [28]) + `openclaw/clawhub:autogit`

---

### #5 — Niche Vertical AI Bot as a Service — 12-20ч

**Примеры:** Vet SOAP Notes $99/клин/мес (WaLead $34k MRR +74% [36]), Therapy SOAP, Plumber Quote $19/мес — микро-SaaS из [36] все строятся за 1-2 нед.
**Стек + репы:** `aiogram` + `Rasa` (NLU) + `midday` (как референс B2B) + `LangBot` (мульти-IM)
**Монетизация:** $39-99/мес/clinic, B2B в 4x прибыльнее B2C [15]

### #6 — Content Repurposer SaaS (Telegram → X/IG/LinkedIn) — 6-10ч

**Боль:** Отправил голос в TG → получил X-thread + LinkedIn post + caption. 2-5k MRR на автомате [37].
**Репы:** `enescingoz/awesome-n8n-templates` → шаблон #5 Local-first Content Repurposer (Ollama+Telegram) [38] — бери готовый, меняй промпт.
**Монетизация:** $15-49/мес, 80% маржа (инференс $5-50/мес [12])

### #7 — OpenClaw Skill Pack → Деньги на ClawHub — 4-8ч на 1 skill

**Боль:** 31k+ skills на ClawHub [39], топ курированный 5.4k [24]. Спрос, но качество мусора — шанс.
**Продукт:** Пак 5 skills: `telegram-stars-payment`, `notion-sync`, `coolify-deploy`, `stripe-recovery`, `tg-mini-app-auth`. Продавай на ClawHub + Toku/Agent marketplace (85% via Stripe Connect [24])
**Стек + репы:** `openclaw/agent-skills` + `VoltAgent/awesome-openclaw-skills` (фильтр) + `skilldock.io` (cross-platform)

### #8 — Self-Hosted Agency Stack (n8n + Local AI) — 10-15ч

**Боль:** Агентство продает исход, не софт [40]: $2-10k/клиент/мес, 60-80% маржа (инфраструктура $30-100/мес [41]).
**Репы:** `n8n self-hosted AI kit` + `keelstamphq/n8n-templates` (spend cap+approval+log) + `myname173/agent-platform` (8 контейнеров)

> **Ранжирование:** 1-2 — самые быстрые (distribution Telegram 0 friction + Stars instant). 3-4 — самые стабильные (SaaS рекуррент). 5-8 — масштаб.

---

## 5. ПОЧАСОВАЯ ХРОНОЛОГИЯ — Что делает ТЫ vs AI-АГЕНТЫ (твои часы vs их 24/7)

> **Ключевая идея:** Твое время — бутылочное горлышко. AI на VPS работает пока ты спишь: 1 твой час = 8-12 часов AI. Поэтому считаем отдельно.

### СТАДИЯ 1: Первые 10 часов твоего времени (Day 0-3) — Цель: живой продукт + первые $ / юзеры

| Твои часы (10ч) | AI-агенты на VPS (параллельно 80-120ч) | Результат |
|---|---|---|
| **Ч 0-1: Выбор ниши + домен** — 1ч: Выбери MVP #1 или #2 из §4, купи `constantin.sh` ($12/год, Cloudflare), заведи BotFather → token | AI idle — ждет токен | Домен + токен |
| **Ч 1-2: VPS + Coolify** — 1ч: `ssh root@vps`, `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`, добавь GitHub App, заведи Postgres+Redis 1-click | AI генерит `AGENTS.md` для проекта (правила, стек) | Инфраструктура готова, как Heroku |
| **Ч 2-4: Промпт MVP** — 2ч: Напиши 1 `PROMPT.md` (что строим, цена Stars, UX), скопируй boilerplate (`aiogram` или `nextjs-template`), `git push` в Coolify | **Claude Code на VPS клонирует, пишет бота/Mini App, коммитит каждые 30 мин** | Первый деплой доступен по URL |
| **Ч 4-6: Платеж + логика** — 2ч: В BotFather включи Stars payments, задай цены (напр. 300 Stars = $3.9 net), проверь тестовый платеж. Для SaaS: Stripe via Coolify | **AI пишет тесты (probe), настраивает n8n workflow: Stars webhook → Postgres → Telegram receipt** | Платеж работает |
| **Ч 6-8: Запуск + 10 юзеров** — 2ч: Пост в 3 TG-канала своей ниши, 5 DM друзьям, включи affiliate (любой юзер может реферить и получать 7% Stars [42]), поставь `Uptime Kuma` | **AI отвечает в боте 24/7 (AstrBot), логирует ошибки, генерит daily digest в твой TG** | Первые 10 юзеров + 1-2 платежа |
| **Ч 8-10: Обратная связь** — 2ч: Прочитай логи, выпиши 3 бага/фичи, обнови `PROMPT.md` для AI | **AI чинит баги (Trace+Forge агенты [28]), деплоит v0.2, шлет тебе summary в 08:00** | v0.2 live, ты потратил только 10ч |

**Что получаешь к концу Стадии 1:**
- Живой URL бот/Mini App + Stars-оплата + логи + мониторинг
- 10-50 юзеров, 1-5 платежей → $13-65 net (1000-5000 Stars) [31]
- AI уже работает 24/7 без тебя

### СТАДИЯ 2: 100 часов твоего времени (Недели 2-6) — Цель: $500-2k MRR, 100-500 юзеров, delegation 80%

| Твои часы (10ч → 100ч, ~15ч/нед) | AI-агенты (24/7, ~600-800ч) | Результат |
|---|---|---|
| **Ч 10-25: Итерации по фидбеку** — 15ч/2 нед: 1ч/день ревью PR от AI, правишь промпты, пишешь 1 тред/нед в X (build in public). Добавляешь 1 фичу/нед (напр. `/memory`, weekly subscription Stars [34]) | **Кодинг нон-стоп:** Claude Code пишет фичи, Lens/Ra review PR, Probe тестит, Forge чинит билды, Log генерит changelog [28]. **n8n генерит контент:** daily TG-post, X-thread из логов | v0.5-1.0, 3-5 фич, weekly план (55.5% subscription revenue [9]) |
| **Ч 25-50: Growth** — 25ч/3 нед: 2ч/нед на outreach: 20 DM/нед в нишевые TG-каналы, 1 Product Hunt launch, 1 пост на Reddit r/TelegramBots + IndieHackers. Настраиваешь Stars affiliate (каждый реферал = 7% lifetime [42]) | **AI-маркетинг:** Beacon-агент генерит SEO-посты, проверяет GSC, шлет холодные email через n8n (280 templates [43]), отвечает на комменты 24/7 | 100-300 юзеров, 20-50 платящих, $260-650 MRR (200k Stars = $2.6k [31] → твой кейс меньше, но тот же паттерн) |
| **Ч 50-75: Второй продукт** — 25ч: Клонируешь MVP #1 → MVP #3 (напр. Cron Monitor) на том же VPS (второй проект в Coolify, общая Postgres). Используешь тот же `ixartz` boilerplate | **AI строит второй SaaS параллельно, переиспользуя auth/billing из первого** | Портфель 2 продукта, как Pieter Levels ($3M/год, 0 сотрудников) [44] |
| **Ч 75-100: Систематизация** — 25ч: Пишешь `SOUL.md` для каждого агента (роли: Coder, Support, Marketer), настраиваешь spend cap per client (keelstamphq template [45]), hash-chained log для аудита, backup в Coolify | **AI-операционка:** Sentinel ловит TS-ошибки, Keeper — миграций, Whisper — потерянные ивенты [28]. Все логи в hash-chain, compliance готов | 200-500 юзеров, $500-2k MRR, ты работаешь 8-10ч/нед, AI — 168ч/нед |

**Что получаешь к концу Стадии 2:**
- 1-2 продукта live, $500-2k MRR, churn <5% (B2B SaaS норма [10])
- AI отвечает 90% саппорта, ты — только стратегия + 1 тред/нед
- Портфель как у @ridark_eth: 35 micro-SaaS → $77k/мес кейс [46] — ты на пути к 2-3

### СТАДИЯ 3: Дальнейшее масштабирование (100ч → ∞, твое время 5-10ч/нед) — Цель: $5-50k MRR, выход или портфель

| Твое время (5-10ч/нед) | AI-агенты (24/7, 168ч/нед) | Стратегия |
|---|---|---|
| **Продукт → Платформа** — 2ч/нед: решаешь, что вынести в skill (напр. Stars-payment skill) и продать на ClawHub (30k+ skills [39]) | AI пакует skills, публикует, отвечает на PR сообщества, версионирует | Новый revenue: ClawHub + Toku marketplace (85% Stripe) [24] |
| **Одна ниша → Портфель** — 3ч/нед: Каждые 4-6 нед клонируешь boilerplate под новую нишу (напр. Vet SOAP → Plumber Quote), переиспользуешь VPS, DB, auth | AI генерит лендинг, SEO, поддержку для каждого продукта (как Marc Lou ShipFast $1M/год, 15 income streams [47]) | 5-10 micro-SaaS × $1-5k MRR = $10-30k MRR, как у Pieter Levels |
| **Ручное → Outcome-агентство** — 2ч/нед: Находишь 1-2 B2B клиента, продаешь исход ($2k/мес), AI делает работу (n8n + Local AI Starter Kit), ты — аккаунт | AI-агент делает 80% доставки, ты — 20% продаж | $2-10k/клиент, 60-80% маржа [41] |
| **Solo → Sale** — 1ч/нед: Когда $10k MRR → листишь на Acquire.com (2-4x ARR), или держишь как lifestyle | AI готовит доки, метрики, дата-рум | Exit $80M Base44 кейс — экстремум, но $50-200k реален за 12-18 мес |

**Масштабирование VPS:**
- $1-5k MRR: 1 VPS €28 (2vCPU/4GB) хватает
- $5-20k MRR: 2 VPS (€28 + €12) + Cloudflare CDN (бесплатно)
- $20k+ MRR: 3 VPS + managed Postgres (Neon/Supabase) + Tinybird analytics (как midday [48])

---

## 6. ПРАКТИЧЕСКИЙ ЧЕК-ЛИСТ — Скопируй в Notion

### За 10 часов (чек-боксы)
- [ ] 0-1ч: Выбран MVP #1/#2/#3, куплен `constantin.sh`, BotFather token
- [ ] 1-2ч: Hetzner CPX32 €15, Coolify installed, Postgres+Redis 1-click
- [ ] 2-4ч: `git clone` boilerplate (aiogram/tma-nextjs/ixartz), `PROMPT.md` написан, `git push` → Coolify
- [ ] 4-6ч: Stars платежи включены, тестовый 100 Stars прошел, n8n webhook → DB
- [ ] 6-8ч: Пост в 3 канала, 5 DM, affiliate вкл, Uptime Kuma
- [ ] 8-10ч: 3 бага выписаны, AI чинит, v0.2 live

### За 100 часов (недели 2-6)
- [ ] Weekly subscription Stars + rewarded ads hybrid [9]
- [ ] 1 PH launch + 1 Reddit post/нед
- [ ] Второй продукт на том же VPS
- [ ] `SOUL.md` для 3 агентов (Coder/Support/Marketer)
- [ ] $500-2k MRR

### Масштаб (100ч+)
- [ ] 1 skill на ClawHub/мес
- [ ] 1 новый micro-SaaS/6 нед
- [ ] 1 outcome-клиент $2k/мес

---

## 7. РИСКИ И АНТИ-ПАТТЕРНЫ

| Риск | Как AI на VPS митигирует |
|---|---|
| **AGPL ловушка (midday)** | Не закрывай код, если форкнул midday. Используй как референс, стартуй с MIT (ixartz/vercel) |
| **Stars 21 день холд** [31] | AI планирует cashflow, шлет напоминалку на 21 день, предлагает Stars→Ads реинвест (0% комиссия [9]) |
| **Apple 30% cut** | AI детектит desktop юзеров (дешевле, $0.013 vs $0.009 net [49]) и пушит им desktop-оплату |
| **VPS упал** | Coolify backup daily + Uptime Kuma алерт в TG (AI чинит рестарт 24/7) |
| **Спам-бан Telegram** | AI rate-limits, соблюдает Bot API лимиты, `awesome-telegram-bots` гайд |
| **Выгорание соло** | Твое время только 5-10ч/нед после стадии 2, остальное — агенты. Как Medvi 1 чел → $401M [19] |

---

## 8. ИТОГОВАЯ РЕКОМЕНДАЦИЯ — С чего начать завтра

**Если у тебя Python:** → **MVP #1 Telegram AI-бот (aiogram 5.9k★)** — 3ч до первого платежа Stars, 280 n8n шаблонов в помощь. Самый быстрый путь к $.

**Если у тебя TS/React:** → **MVP #2 Mini App (nextjs-template 370★)** — 6ч, красивый UI из коробки, viral в TG.

**Если у тебя SaaS-опыт:** → **MVP #3 Cron Monitor (ixartz 12.9k★ MIT)** — 8ч, доказанный $14k MRR, спишь спокойно.

**Универсальный старт (мой совет):**
1. День 1 (2ч твоего времени): VPS + Coolify + `aiogram` бот + Stars
2. День 2-3 (AI 48ч): бот отвечает, принимает 300 Stars, шлет receipt
3. День 7: PH launch Mini App версии того же бота (тот же бэкенд, другой фронт)
4. Неделя 3: клон в Cron SaaS на том же VPS (второй проект Coolify)

Через 100ч твоего времени + 800ч AI у тебя 2 продукта, $500-2k MRR, и фабрика 24/7.

> **Все репо выше — бесплатны (MIT/Apache2, кроме midday AGPL). Делегируй максимум: ты — архитектор, AI-агенты на VPS — строители. 1 твой час = 10 их часов. Так строят Base44 ($80M, 1 чел) и Medvi ($401M, 1 чел).**

---

## 9. Источники (20.10.2026)

[1] Agent Payments x402, [2] JetBrains 39% Claude Code, [3] AI agent $52.6B 2030, [4] Micro-SaaS $59.6B 2030, [5] awesome-telegram-ai-bots 2026-04-18, [6] Telegram 500M Mini Apps, [7] PropellerAds 1.44B→150M, [8] Catizen $35M, [9] Stars monet 2026 hybrid 60-70% ads, weekly 55.5%, [10] Healthchecks $14k MRR, [11] Micro-SaaS median $136, [12] 14% vs 30-50% AI-native, [13] Submagic $8M, [14] Solo 36.3% Forbes, [15] Stripe Atlas 63% Q2'26, [16] $300-500 vs $80k-120k, [17] 38% 7-figure solo, [18] Base44 $80M, [19] Medvi $401M, [20] LangBot 15.4k, [21] agent-platform 8 cont 24 workflows, [22] VPS specs, [23] Hermes 247k $5 VPS, [24] awesome-openclaw-skills 52.9k, [25] Hermes $5 guide, [26] Coolify 61k, [27] Dokploy 37k, [28] awesome-openclaw-agents 162, [29] mb_support_bot, [30] Stars $0.013, [31] 1000 Stars $13, [32] herval/cliobot, [33] mini-woo, [34] Stars subscriptions, [35] Changelog SaaS $19-49, [36] Vet SOAP $99, [37] Content repurposer $2-5k MRR, [38] 5 local-first n8n workflows, [39] ClawHub 31k, [40] Sell outcome not software, [41] $30-100/mo infra, [42] Hub Aggregator 7% revshare, [43] awesome-n8n-templates 280+, [44] Pieter Levels $3M/0 emp, [45] keelstamphq n8n, [46] 35 micro-SaaS $77k/mo, [47] Marc Lou 15 streams, [48] midday Tinybird, [49] Desktop $0.013 vs mobile $0.009

*Полный каталог реп с лицензиями и командами установки — в §2. Копируй repo name в GitHub → Clone → Deploy via Coolify 1-click.*
