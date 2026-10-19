# Модель делегации: Человек vs AI-агенты на VPS (2026)

> 1 твой час = 8-12 часов AI. Твоя задача — не писать код, а принимать решения, которые меняют деньги.

## Принцип

| Уровень | Кто | Стоимость | Что делает |
|---|---|---|---|
| **L1: Стратегия** | Ты | €100/ч | Ниша, цена, оффер, `SOUL.md` / `AGENTS.md` — 100% ты |
| **L2: Исполнение** | AI на VPS 24/7 | ~€0.50/ч | Код, тесты, деплой, саппорт, контент, outreach — 80-90% AI |
| **L3: Контроль** | Ты | 1ч/день | Ревью PR, чтение логов, 1 тред в X — 10% времени |

## Таблица делегации по задачам

| Задача | Ты (5-10ч/нед) | AI-агент (168ч/нед) | Репо/инструмент |
|---|---|---|---|
| **Идея + цена** | Пишешь 1 `PROMPT.md`, выбираешь Stars $9.75/750 Stars | — | — |
| **Код MVP** | Промпт + ревью PR 15 мин/день | Claude Code пишет, OpenHands тестит, Forge чинит билды | `openclaw/openclaw` 300k★ |
| **Дизайн** | Выбираешь из 280+ Coolify templates | v0/Lovable генерит лендинг | `coolify` 61k★ |
| **Контент/SEO** | 1 пост/нед в X (build in public) | Beacon генерит блог, GSC, постит | `awesome-openclaw-agents` 162 агента |
| **Поддержка** | Только escalated (>95% AI) | AstrBot/Botpress 24/7 в TG | `AstrBot` 41.9k★ |
| **Деплой** | `git push` | Coolify auto-build+SSL+backup | `coolify` / `dokploy` 37k★ |
| **Продажи** | 1 демо/день | n8n триггерит DMs, ClawMarket продает | `awesome-n8n-templates` 280+ |
| **Платежи** | Подключаешь Stars 1 раз | n8n webhook → Postgres → receipt | Stars $0.013/Star |

## Роли AI-агентов (SOUL.md)

Создай 3 файла `agents/` на VPS, каждый — отдельный контейнер:

### 1. Coder (Claude Code + Hermes)
```
SOUL: Ты — senior TS/Python, пишешь только через тесты, коммитишь осмысленно
SKILLs: agent-commons, handoff, beam, probe
MCP: GitHub, Postgres, Notion
```

### 2. Support (AstrBot + Botpress)
```
SOUL: Отвечай за <2с, эскалируй если не знаешь, логируй всё в Postgres
SKILLs: telegram-mcp, notion-sync
```

### 3. Marketer (n8n + Beacon)
```
SOUL: 1 тред/день, 1 SEO-пост/нед, холодные DM 20/нед, не спамь
SKILLs: aladdn-market, clawsocial
```

## Стоимость vs найм

| Конфиг | VPS | AI API | /мес | Заменяет |
|---|---|---|---|---|
| Minimal (1 бот) | €12 | $20 | ~€35 | Фрилансер $1k |
| Standard (бот+App+SaaS) | €28 | $100 | ~€80 | Команда $5k |
| Full (3+ агента) | €84 | $250 | ~€250 | Стартап $20k |

OpenClaw $300-500/мес = $80-120k payroll (50x leverage).

## Чек-лист внедрения (1ч)

- [ ] VPS: `docker compose up -d` из `infra/docker-compose.yml`
- [ ] Создай 3 `SOUL.md` в `/data/agents/`
- [ ] Подключи Telegram token + OpenAI key в `.env`
- [ ] Настрой n8n: Telegram trigger → AI → Postgres → Telegram answer
- [ ] Проверь: отправь `/ask` в бот — AI ответил за <3с, лог в Postgres

> Дальше только 1ч/день ревью. Остальное 24/7 без тебя.
