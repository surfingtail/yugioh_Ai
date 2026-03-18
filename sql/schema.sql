PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS cards (
    card_id INTEGER PRIMARY KEY,
    name_ko TEXT NOT NULL,
    desc_ko TEXT,
    pendulum_desc_ko TEXT,

    card_kind TEXT NOT NULL
        CHECK (card_kind IN ('Monster', 'Spell', 'Trap')),

    spell_type TEXT
        CHECK (spell_type IN ('Normal', 'Field', 'Equip', 'Quick-Play', 'Continuous', 'Ritual')),

    trap_type TEXT
        CHECK (trap_type IN ('Normal', 'Continuous', 'Counter')),

    monster_type TEXT
        CHECK (monster_type IN ('Normal', 'Effect', 'Fusion', 'Synchro', 'Xyz', 'Ritual', 'Link')),

    is_pendulum INTEGER NOT NULL DEFAULT 0
        CHECK (is_pendulum IN (0, 1)),

    attribute TEXT
        CHECK (attribute IN ('WATER', 'FIRE', 'WIND', 'EARTH', 'LIGHT', 'DARK', 'DIVINE')),

    race TEXT
        CHECK (race IN (
            'INSECT', 'DINOSAUR', 'MACHINE', 'DRAGON', 'SPELLCASTER', 'AQUA',
            'THUNDER', 'WINGEDBEAST', 'CYBERSE', 'PSYCHIC', 'PLANT', 'FIEND',
            'ROCK', 'BEAST', 'BEASTWARRIOR', 'FISH', 'ZOMBIE', 'WARRIOR',
            'FAIRY', 'REPTILE', 'SEASERPENT', 'PYRO', 'WYRM', 'ILLUSION',
            'DIVINEBEAST', 'CREATORGOD'
        )),

    is_tuner INTEGER NOT NULL DEFAULT 0
        CHECK (is_tuner IN (0, 1)),

    is_special_summon INTEGER NOT NULL DEFAULT 0
        CHECK (is_special_summon IN (0, 1)),

    is_flip INTEGER NOT NULL DEFAULT 0
        CHECK (is_flip IN (0, 1)),

    is_toon INTEGER NOT NULL DEFAULT 0
        CHECK (is_toon IN (0, 1)),

    is_spirit INTEGER NOT NULL DEFAULT 0
        CHECK (is_spirit IN (0, 1)),

    is_union INTEGER NOT NULL DEFAULT 0
        CHECK (is_union IN (0, 1)),

    is_gemini INTEGER NOT NULL DEFAULT 0
        CHECK (is_gemini IN (0, 1)),

    level INTEGER CHECK (level >= 0),
    rank INTEGER CHECK (rank >= 0),
    pendulum_scale INTEGER CHECK (pendulum_scale >= 0),

    link_marker_count INTEGER
        CHECK (link_marker_count BETWEEN 0 AND 8),

    link_marker INTEGER
        CHECK (link_marker BETWEEN 0 AND 255), -- 좌측 하단부터 반시계방향 비트마스크

    atk INTEGER CHECK (atk >= 0),
    defense INTEGER CHECK (defense >= 0),

    is_official_translation INTEGER NOT NULL DEFAULT 0
        CHECK (is_official_translation IN (0, 1))
);