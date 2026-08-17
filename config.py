# --- Основные настройки ---
# Токен бота
BOT_TOKEN = "8956232681:AAHMiBNrTPiLg-a3ACr-dpZP-yIG9EPJAoE"

# Список ID администраторов
ADMINS = [7921743592,8207980755]

# --- API Ключи (Заполните свои данные) ---
CRYPTO_PAY_TOKEN = "548204:AAZOXSPMBWOj3XO29UyRcrxpgxlzujtetPO" # Токен от @CryptoBot (Crypto Pay API)
XROCKET_API_KEY = "e2cb39713d428809d8f1924c8"  # API Key от @xRocket

# --- Лимиты ---
MIN_DEPOSIT = 0.2  # Минимальное пополнение в 💰
MIN_WITHDRAW = 0.15 # Минимальный вывод в 💰
MAX_BET = 1000.0    # Максимальная ставка в 💰

# --- Ссылки ---
CHANNEL_URL = "https://t.me/DuckBets"  # Ссылка на канал
SUPPORT_URL = "https://t.me/zaniks_coder"  # Ссылка на поддержку/помощь
SITE_URL = "https://example.com"       # Ссылка на сайт
CHAT_URL = "https://t.me/duckcasn"     # Ссылка на чат
ALERTS_CHANNEL = "@duckbets_game"        # Канал для крупных выигрышей/выводов
REFERRAL_LINK_TEMPLATE = "t.me/spins?start=invite_3mCfBuOatgwy" # Пример реф ссылки

# --- Тексты ---
TEXTS = {
    "ru": {
        "welcome": (
            f"<b>Привет, добро пожаловать в @spins</b>\n\n"
            f"<blockquote>Подписывайся на <a href='{CHANNEL_URL}'>наш канал</a> чтобы следить за новостями и конкурсами.</blockquote>"
        ),
        "profile": (
            "<b>#{player_id} {name}</b>\n\n"
            "<blockquote><b><tg-emoji emoji-id=\"5449624985301717991\">💳</tg-emoji> Баланс — {balance:.2f} 💰\n"
            "Ваш VIP прогресс — {rank_progress:.0f}%\n"
            "{progress_bar}\n"
            "{current_rank} → {next_rank}\n\n"
            "<tg-emoji emoji-id=\"5452042536493288421\">📊</tg-emoji> Оборот — {turnover:.2f} 💰\n"
            "<tg-emoji emoji-id=\"5451807640436903198\">🎰</tg-emoji> Сыграно — {bets} ставок\n"
            "<tg-emoji emoji-id=\"5312462735097764089\">👑</tg-emoji> Аккаунту — {days}</b></blockquote>"
        ),
        "chats": "<blockquote>🗨 Игровые чаты это отличное место чтобы найти друзей, обсудить игру или поднять денег в конкурсах и раздачах!</blockquote>",
        "referral": (
            "<blockquote>🐈‍⬛ <b>Реф. система — 3 уровня</b></blockquote>\n\n"
            "1 <tg-emoji emoji-id=\"5451778692357327880\">📈</tg-emoji> 60% | 0 <tg-emoji emoji-id=\"5452145345125456281\">🎁</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>\n"
            "2 <tg-emoji emoji-id=\"5451778692357327880\">📈</tg-emoji> 30% | 0 <tg-emoji emoji-id=\"5452145345125456281\">🎁</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>\n"
            "3 <tg-emoji emoji-id=\"5451778692357327880\">📈</tg-emoji> 10% | 0 <tg-emoji emoji-id=\"5452145345125456281\">🎁</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>\n\n"
            "<b>Ваша ссылка</b>\n"
            f"<code>{REFERRAL_LINK_TEMPLATE}</code>\n\n"
            "<b>Общий доход</b>\n"
            "0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>"
        ),
        "play": (
            "<b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji> Выбирайте мини-игру!</b>\n\n"
            "<blockquote>Баланс — {balance:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji>\n"
            "Ставка — {bet:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></blockquote>\n\n"
            "<i>Пополняй и сыграй на реальные деньги!</i>"
        ),
        "modes_menu": (
            "<b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji> Выбирайте мини-игру!</b>\n\n"
            "<blockquote>Баланс — {balance:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji>\n"
            "Ставка — {bet:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></blockquote>\n\n"
            "<i>Пополняй и сыграй на реальные деньги</i>"
        ),
        "mines_main": (
            "<b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji> Мины</b>\n\n"
            "Игрок #{player_id}\n"
            "<blockquote><tg-emoji emoji-id=\"5451845260055450038\">💰</tg-emoji> Баланс — {balance:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji>\n"
            "Ставка — {bet:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></blockquote>\n\n"
            "Выбрано — {mines} <tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji>"
        ),
        "mines_select": (
            "<tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji><b>Выберите количество</b>\n\n"
            "Выбрано — <b>{mines}<tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji></b>\n\n"
            "<blockquote>{coefs}</blockquote>"
        ),
        "mines_playing": (
            "<blockquote><b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji>Мины · {mines} 🎀</b></blockquote>\n\n"
            "<b>{bet:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji> × {coef:.2f} ➔ {win:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></b>\n\n"
            "<blockquote>{coefs}</blockquote>"
        ),
        "deposit_method": "<tg-emoji emoji-id=\"5451985838630014131\">💎</tg-emoji> Выберите способ пополнения",
        "enter_deposit_amount": "<tg-emoji emoji-id=\"5451985838630014131\">💎</tg-emoji> Введите сумму пополнения в <b><tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></b>\n\n<i>Минимальная сумма: {min_amount:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></i>",
        "enter_withdraw_amount": "<tg-emoji emoji-id=\"5451985838630014131\">💎</tg-emoji> Введите сумму вывода в <b><tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></b>\n\n<i>Минимальная сумма: {min_amount:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></i>",
        "deposit_created": "<tg-emoji emoji-id=\"5303170015007119865\">⭐️</tg-emoji> Нажмите ниже, чтобы пополнить баланс",
        "check_payment": "Проверить оплату",
        "payment_success": "<tg-emoji emoji-id=\"5264890676599884371\">🔼</tg-emoji> Баланс успешно пополнен на <b>{amount:.2f} 💰</b>!",
        "payment_not_found": " Оплата не найдена. Пожалуйста, оплатите счет и нажмите кнопку еще раз.",
        "error_min_deposit": " Минимальная сумма пополнения — {min_amount:.2f} 💰",
        "error_min_withdraw": " Минимальная сумма вывода — {min_amount:.2f} 💰",
        "language_select": "🌐 Выберите язык бота",
        "privacy": (
            "<b>🥷 Приватность</b>\n\n"
            "— <i>Крупные ставки и победы в @duckbets_game</i>\n"
            "— <i>Топ игроков по обороту и балансу</i>\n"
            "— <i>Ставки в чатах</i>\n\n"
            "Отображается {display_mode}"
        ),
        "privacy_set_nickname": "📝 Введите ваш новый псевдоним (до 15 символов):",
        "nickname_updated": "✅ Псевдоним успешно обновлен!",
        "privacy_updated": "✅ Настройки приватности обновлены!",
        "stats_text": (
            "<tg-emoji emoji-id=\"5452042536493288421\">📊</tg-emoji> <b>Статистика {name}</b>\n\n"
            "<tg-emoji emoji-id=\"5451811677706167149\">⚽️</tg-emoji> Сыграно — {bets} ставок\n"
            "<tg-emoji emoji-id=\"5449624985301717991\">💳</tg-emoji> Оборот — {turnover:.2f} 💰\n"
            "<tg-emoji emoji-id=\"5449880441366548359\">🃏</tg-emoji> Аккаунту — {days} {days_label}\n\n"
            "<tg-emoji emoji-id=\"5264890676599884371\">🔼</tg-emoji> Пополнений — {deposits:.2f} 💰\n"
            "<tg-emoji emoji-id=\"5452147973645439296\">🔽</tg-emoji> Выводов — {withdrawals:.2f} 💰"
        ),
        "buttons": {
            "play": "🎮 Играть",
            "chats": "💬 Игровые чаты",
            "profile": "👤 Профиль",
            "referral": "👥 Реф. программа",
            "language": "🌐 Язык",
            "back": "⬅️ Назад",
            "deposit": "💸 Пополнить",
            "withdraw": "📥 Вывести",
            "stats": "📊 Статистика",
            "privacy": "🥷 Приватность",
            "bonuses": "🍬 Бонусы",
            "main_chat": "🇷🇺 Основной чат",
            "claim_ref": "Забрать на баланс · 0.00 ",
            "invite_friend": "Пригласить друга",
            "details": "Подробнее",
            "game_dice": "🎲",
            "game_soccer": "⚽",
            "game_basket": "🏀",
            "game_darts": "🎯",
            "game_bowling": "🎳",
            "game_slots": "🎰",
            "provider_tg": "⛄ Telegram",
            "provider_custom": "🐳 Авторские",
            "site": " Сайт",
            "change_bet": "✏️ Изменить ставку",
            "crypto_bot": " Crypto Bot",
            "xrocket": " xRocket",
            "lang_ru": "🇷🇺 RU",
            "lang_en": "🇺🇸 EN",
            "pay": "Пополнить · {amount:.2f} 💰",
            "change_amount": "🔄 Изменить сумму",
            "settings": "⚙️ Настройки",
            "transactions": "📠 Транзакции",
            "game_history": "🔬 История игр",
            "modes": "💣 Режимы",
            "game_mines": "💣 Мины",
            "game_tower": "🗼 Башня"
        }
    },
    "en": {
        "welcome": (
            f"<b>Hello, welcome to @spins</b>\n\n"
            f"<blockquote>Subscribe to <a href='{CHANNEL_URL}'>our channel</a> to follow news and contests.</blockquote>"
        ),
        "profile": (
            "<b>#{player_id} {name}</b>\n\n"
            "<blockquote><b><tg-emoji emoji-id=\"5449624985301717991\">💳</tg-emoji> Balance — {balance:.2f} 💰\n"
            "Your VIP progress — {rank_progress:.0f}%\n"
            "{progress_bar}\n"
            "{current_rank} → {next_rank}\n\n"
            "<tg-emoji emoji-id=\"5452042536493288421\">📊</tg-emoji> Turnover — {turnover:.2f} 💰\n"
            "<tg-emoji emoji-id=\"5451807640436903198\">🎰</tg-emoji> Played — {bets} bets\n"
            "<tg-emoji emoji-id=\"5312462735097764089\">👑</tg-emoji> Account — {days}</b></blockquote>"
        ),
        "chats": "<blockquote>🗨 Game chats are a great place to find friends, discuss the game and raise money in contests and giveaways!</blockquote>",
        "referral": (
            "<blockquote>🐈‍⬛ <b>Ref. system — 3 levels</b></blockquote>\n\n"
            "1 <tg-emoji emoji-id=\"5451778692357327880\">📈</tg-emoji> 60% | 0 <tg-emoji emoji-id=\"5452145345125456281\">🎁</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>\n"
            "2 <tg-emoji emoji-id=\"5451778692357327880\">📈</tg-emoji> 30% | 0 <tg-emoji emoji-id=\"5452145345125456281\">🎁</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>\n"
            "3 <tg-emoji emoji-id=\"5451778692357327880\">📈</tg-emoji> 10% | 0 <tg-emoji emoji-id=\"5452145345125456281\">🎁</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji> | 0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>\n\n"
            "<b>Your link</b>\n"
            f"<code>{REFERRAL_LINK_TEMPLATE}</code>\n\n"
            "<b>Total revenue</b>\n"
            "0.00 <tg-emoji emoji-id=\"5451754391432366821\">💰</tg-emoji>"
        ),
        "play": (
            "<b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji> Choose a mini-game!</b>\n\n"
            "<blockquote>Balance — {balance:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji>\n"
            "Bet — {bet:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></blockquote>\n\n"
            "<i>Top up and play for real money!</i>"
        ),
        "modes_menu": (
            "<b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji> Choose a mini-game!</b>\n\n"
            "<blockquote>Balance — {balance:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji>\n"
            "Bet — {bet:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></blockquote>\n\n"
            "<i>Top up and play for real money</i>"
        ),
        "mines_main": (
            "<b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji> Mines</b>\n\n"
            "Player #{player_id}\n"
            "<blockquote><tg-emoji emoji-id=\"5451845260055450038\">💰</tg-emoji> Balance — {balance:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji>\n"
            "Bet — {bet:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></blockquote>\n\n"
            "Selected — {mines} <tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji>"
        ),
        "mines_select": (
            "<tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji><b>Select quantity</b>\n\n"
            "Selected — <b>{mines}<tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji></b>\n\n"
            "<blockquote>{coefs}</blockquote>"
        ),
        "mines_playing": (
            "<blockquote><b><tg-emoji emoji-id=\"5452018153963948977\">💣</tg-emoji>Mines · {mines} 🎀</b></blockquote>\n\n"
            "<b>{bet:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji> × {coef:.2f} ➔ {win:,.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></b>\n\n"
            "<blockquote>{coefs}</blockquote>"
        ),
        "deposit_method": "<tg-emoji emoji-id=\"5451985838630014131\">💎</tg-emoji> Choose deposit method",
        "enter_deposit_amount": "<tg-emoji emoji-id=\"5451985838630014131\">💎</tg-emoji> Enter deposit amount in <b><tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></b>\n\n<i>Minimum amount: {min_amount:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></i>",
        "enter_withdraw_amount": "<tg-emoji emoji-id=\"5451985838630014131\">💎</tg-emoji> Enter withdrawal amount in <b><tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></b>\n\n<i>Minimum amount: {min_amount:.2f} <tg-emoji emoji-id=\"5452157517062770940\">💸</tg-emoji></i>",
        "deposit_created": "<tg-emoji emoji-id=\"5303170015007119865\">⭐️</tg-emoji> Click below to top up your balance",
        "check_payment": "Check Payment",
        "payment_success": "<tg-emoji emoji-id=\"5264890676599884371\">🔼</tg-emoji> Balance successfully topped up by <b>{amount:.2f} 💰</b>!",
        "payment_not_found": " Payment not found. Please pay the invoice and click the button again.",
        "error_min_deposit": " Minimum deposit amount is {min_amount:.2f} 💰",
        "error_min_withdraw": " Minimum withdrawal amount is {min_amount:.2f} 💰",
        "language_select": "🌐 Choose bot language",
        "privacy": (
            "<b>🥷 Privacy</b>\n\n"
            "— <i>Big bets and wins in @wins_alerts</i>\n"
            "— <i>Top players by turnover and balance</i>\n"
            "— <i>Bets in chats</i>\n\n"
            "Displayed: {display_mode}"
        ),
        "privacy_set_nickname": "📝 Enter your new pseudonym (up to 15 characters):",
        "nickname_updated": "✅ Pseudonym successfully updated!",
        "privacy_updated": "✅ Privacy settings updated!",
        "stats_text": (
            "<tg-emoji emoji-id=\"5452042536493288421\">📊</tg-emoji> <b>Statistics {name}</b>\n\n"
            "<tg-emoji emoji-id=\"5451811677706167149\">⚽️</tg-emoji> Played — {bets} bets\n"
            "<tg-emoji emoji-id=\"5449624985301717991\">💳</tg-emoji> Turnover — {turnover:.2f} 💰\n"
            "<tg-emoji emoji-id=\"5449880441366548359\">🃏</tg-emoji> Account — {days} {days_label}\n\n"
            "<tg-emoji emoji-id=\"5264890676599884371\">🔼</tg-emoji> Deposits — {deposits:.2f} 💰\n"
            "<tg-emoji emoji-id=\"5452147973645439296\">🔽</tg-emoji> Withdrawals — {withdrawals:.2f} 💰"
        ),
        "buttons": {
            "play": "🎮 Play",
            "chats": "💬 Game Chats",
            "profile": "👤 Profile",
            "referral": "👥 Referral Program",
            "language": "🌐 Language",
            "back": "⬅️ Back",
            "deposit": "💸 Deposit",
            "withdraw": "📥 Withdraw",
            "stats": "📊 Statistics",
            "privacy": "🥷 Privacy",
            "bonuses": "🍬 Bonuses",
            "main_chat": "🇺🇸 Main Chat",
            "claim_ref": "Claim to balance · 0.00 💰",
            "invite_friend": "Invite a friend",
            "details": "Details",
            "game_dice": "🎲",
            "game_soccer": "⚽",
            "game_basket": "🏀",
            "game_darts": "🎯",
            "game_bowling": "🎳",
            "game_slots": "🎰",
            "provider_tg": "⛄ Telegram",
            "provider_custom": "🐳 Custom",
            "site": "❄️ Site",
            "change_bet": "✏️ Change bet",
            "crypto_bot": " Crypto Bot",
            "xrocket": " xRocket",
            "lang_ru": "🇷🇺 RU",
            "lang_en": "🇺🇸 EN",
            "pay": "Deposit · {amount:.2f} 💰",
            "change_amount": "🔄 Change amount",
            "settings": "⚙️ Settings",
            "transactions": "📠 Transactions",
            "game_history": "🔬 Game History",
            "modes": "💣 Modes",
            "game_mines": "💣 Mines",
            "game_tower": "🗼 Tower"
        }
    }
}
