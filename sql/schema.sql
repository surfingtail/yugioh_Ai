PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS cards (
    card_id INTEGER PRIMARY KEY,
    name_ko TEXT NOT NULL,
    desc_ko TEXT,
    pendulum_desc_ko TEXT,

    card_kind TEXT NOT NULL
        CHECK (card_kind IN ('몬스터', '마법', '함정')),

    spell_type TEXT
        CHECK (spell_type IN ('일반', '필드', '장비', '속공', '지속', '의식')),

    trap_type TEXT
        CHECK (trap_type IN ('일반', '지속', '카운터')),

    monster_type TEXT
        CHECK (monster_type IN ('일반', '효과', '융합', '싱크로', '엑시즈', '의식', '링크')),

    is_pendulum INTEGER NOT NULL DEFAULT 0
        CHECK (is_pendulum IN (0, 1)),

    attribute TEXT
        CHECK (attribute IN ('물', '화염', '바람', '땅', '빛', '어둠', '신')),

    race TEXT
        CHECK (race IN (
            '곤충족', '공룡족', '기계족', '드래곤족', '마법사족', '물족',
            '번개족', '비행야수족', '사이버스족', '사이킥족', '식물족', '악마족',
            '암석족', '야수족', '야수전사족', '어류족', '언데드족', '전사족',
            '천사족', '파충류족', '해룡족', '화염족', '환룡족', '환상마족',
            '환신야수족', '창조신족'
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
        CHECK (link_marker BETWEEN 0 AND 255), -- 좌측 상단부터 시계방향 비트마스크 1:좌상, 2:상, 4:우상, 8:우, 16:우하, 32:하, 64:좌하, 128:좌

    atk INTEGER CHECK (atk >= 0),
    defense INTEGER CHECK (defense >= 0),

    is_official_translation INTEGER NOT NULL DEFAULT 0
        CHECK (is_official_translation IN (0, 1))
);