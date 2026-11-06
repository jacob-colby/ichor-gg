---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: Aspect of Heartbreak
  aspect_pick_rate: 0.82
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.37
    win_rate: 0.67
    alternates:
    - name: Book of Thoth
      pick_rate: 0.22
      win_rate: 0.58
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.35
  - name: Rod of Tahuti
    pick_rate: 0.17
    win_rate: 0.64
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.7
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.59
  - name: Spear of the Magus
    pick_rate: 0.09
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.19
      win_rate: 0.67
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.23
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.24
      win_rate: 0.62
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.75
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.67
  - name: Helm of Darkness
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.2
      win_rate: 0.87
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.25
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.34
    win_rate: 0.66
  - name: Sands Of Time
    pick_rate: 0.19
    win_rate: 0.53
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.73
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-11-06'
  god_win_rate: 0.593939393939394
  god_matches_won: 98
  god_matches_played: 165
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, Genji''s
    Guard, Freya''s Tears, Breastplate of Valor, Shield of the Phoenix, Lotus Sickle,
    Helm of Radiance, Draconic Scale, Blood-Bound Book, Oni Hunter''s Garb, Erosion,
    Eye of Providence, Shifter''s Shield, Ancient Signet, Screeching Gargoyle, Chronos''
    Pendant, Midgardian Mail, Polynomicon, Dreamer''s Idol, Jade Scepter, Stone of
    Binding, Leviathan''s Hide, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.33
    Helm of Darkness:
      total: 0.59
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, Lotus Sickle,
    Breastplate of Valor, Freya''s Tears, Ancient Signet, Death Metal, Blood-Bound
    Book, Oni Hunter''s Garb, Helm of Radiance, Polynomicon, Shield of the Phoenix,
    Draconic Scale, Chronos'' Pendant, Dreamer''s Idol, Doom Orb, Screeching Gargoyle,
    Jade Scepter, Erosion, Bancroft''s Talon, Eye of Providence, Triton''s Conch,
    Spear of the Magus.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.48
      win: 0.58
      pick: 0.22
      fit: 0.24
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.26
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.38
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.35
    Helm of Darkness:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Kinetic Cuirass,
    Freya''s Tears, Breastplate of Valor, Lotus Sickle, Shield of the Phoenix, Blood-Bound
    Book, Helm of Radiance, Oni Hunter''s Garb, Dreamer''s Idol, Draconic Scale, Screeching
    Gargoyle, Death Metal, Ancient Signet, Chronos'' Pendant, Erosion, Polynomicon,
    Eye of Providence, Doom Orb, Midgardian Mail, Shifter''s Shield, Leviathan''s
    Hide, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.33
    Helm of Darkness:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.37
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Helm of Darkness
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Blood-Bound Book, Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Freya''s Tears,
    Phoenix Feather, Bancroft''s Talon, Yogi''s Necklace, Breastplate of Valor, Lotus
    Sickle, Rod of Asclepius, Soul Locket, Draconic Scale, Oni Hunter''s Garb, Helm
    of Radiance, Sphere of Negation, Regrowth Striders, Erosion, Eye of Providence,
    Chronos'' Pendant, Spear of the Magus, Chandra''s Grace.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.33
    Helm of Darkness:
      total: 0.58
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.47
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.62
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.94
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Genji''s Guard, Kinetic
    Cuirass, Screeching Gargoyle, Stone of Binding, Freya''s Tears, Void Stone, Void
    Shield, Breastplate of Valor, Dreamer''s Idol, Lotus Sickle, Shield of the Phoenix,
    Blood-Bound Book, Helm of Radiance, Doom Orb, Oni Hunter''s Garb, Draconic Scale,
    The World Stone, Ancient Signet, Erosion, Eye of Providence, Chronos'' Pendant,
    Spear of the Magus, Polynomicon.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.24
    Spear of Desolation:
      total: 0.61
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.55
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.45
    Helm of Darkness:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.42
    Obsidian Shard:
      total: 0.57
      efficiency: 0.53
      win: 0.63
      pick: 0.38
      fit: 0.55
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Eros' Bow
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Freya''s Tears, Breastplate of Valor, Nimble Ring, Lotus Sickle, Shield
    of the Phoenix, Blood-Bound Book, Bragi''s Harp, Helm of Radiance, Oni Hunter''s
    Garb, Ancient Signet, Eros'' Bow, Draconic Scale, Death Metal, Polynomicon, Screeching
    Gargoyle, Bracer of The Abyss, Chronos'' Pendant, Erosion, Midgardian Mail, Eye
    of Providence, Spear of the Magus.'
  slot_scores:
    Nimble Ring:
      total: 0.52
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.51
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.29
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.21
    Helm of Darkness:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.32
    Eros' Bow:
      total: 0.51
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Helm of Darkness
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Soul Gem, Amanita
    Charm, Freya''s Tears, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix,
    Gluttonous Grimoire, Lotus Sickle, Screeching Gargoyle, Chronos'' Pendant, Gladiator''s
    Shield, Oni Hunter''s Garb, Draconic Scale, Prophetic Cloak, Blood-Bound Book,
    Helm of Radiance, Erosion, Eye of Providence, Gem of Focus, Heartwood Charm, Midgardian
    Mail, Shifter''s Shield, Ancient Signet, Stone of Binding, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.48
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.2
    Helm of Darkness:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.34
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, Jotunn''s Revenge, Amanita
    Charm, Soul Gem, Genji''s Guard, Gluttonous Grimoire, Kinetic Cuirass, Shield
    Splitter, Tyrfing, Freya''s Tears, The Reaper, Breastplate of Valor, Golden Blade,
    Runeforged Hammer, Hydra''s Lament, Lotus Sickle, Shield of the Phoenix, Death
    Metal, Blood-Bound Book, Helm of Radiance, The Crusher, Bragi''s Harp, Oni Hunter''s
    Garb, Nimble Ring, Heartseeker, Ancient Signet, Draconic Scale, Screeching Gargoyle,
    Polynomicon, Titan''s Bane, Tekko-Kagi, Chronos'' Pendant, Erosion, Dreamer''s
    Idol, Toxic Blade, Eye of Providence, Arondight, Spear of the Magus.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.35
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.26
    Helm of Darkness:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Soul Gem, Jotunn''s
    Revenge, Gluttonous Grimoire, Genji''s Guard, Kinetic Cuirass, Berserker''s Shield,
    Freya''s Tears, Shield Splitter, Breastplate of Valor, The Reaper, Lotus Sickle,
    Shield of the Phoenix, Blood-Bound Book, Runeforged Hammer, Hydra''s Lament, Death
    Metal, Helm of Radiance, Oni Hunter''s Garb, Ancient Signet, Draconic Scale, The
    Crusher, Tyrfing, Chronos'' Pendant, Polynomicon, Heartseeker, Dreamer''s Idol,
    Screeching Gargoyle, Erosion, Eye of Providence, Jade Scepter, Midgardian Mail,
    Shifter''s Shield, Titan''s Bane, Stone of Binding, Leviathan''s Hide, Triton''s
    Conch, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.41
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.31
    Helm of Darkness:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.28
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Helm of Darkness
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Kinetic
    Cuirass, Genji''s Guard, Freya''s Tears, Breastplate of Valor, Shield of the Phoenix,
    Lotus Sickle, Helm of Radiance, Draconic Scale, Blood-Bound Book, Oni Hunter''s
    Garb, Erosion, Eye of Providence, Chronos'' Pendant, Spear of the Magus, Shifter''s
    Shield, Ancient Signet, Screeching Gargoyle, Midgardian Mail, Polynomicon, Dreamer''s
    Idol, Jade Scepter, Stone of Binding, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.61
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.6
      efficiency: 0.6
      win: 0.67
      pick: 0.37
      fit: 0.46
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.64
      pick: 0.23
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
