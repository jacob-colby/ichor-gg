---
type: smite-build
god: Hades
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Daybreak Gavel
    pick_rate: 0.31
    win_rate: 0.62
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.58
  - name: The World Stone
    pick_rate: 0.32
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.57
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.73
  - name: Shifter's Shield
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: The World Stone
      pick_rate: 0.27
      win_rate: 0.68
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.7
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.61
    - name: Soul Gem
      pick_rate: 0.06
      win_rate: 0.7
  - name: Rod of Tahuti
    pick_rate: 0.21
    win_rate: 0.68
    alternates:
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.68
    - name: Obsidian Shard
      pick_rate: 0.05
      win_rate: 0.53
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.53
    alternates:
    - name: Dreamer's Idol
      pick_rate: 0.07
      win_rate: 0.62
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.92
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.33
    win_rate: 0.64
  - name: Conduit Gem
    pick_rate: 0.29
    win_rate: 0.49
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/hades/
  last_verified: '2026-08-16'
  god_win_rate: 0.5982658959537572
  god_matches_won: 207
  god_matches_played: 346
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Genji''s
    Guard, Nimble Ring, The Cosmic Horror, Spear of the Magus, Breastplate of Valor,
    Shield of the Phoenix, Oni Hunter''s Garb, Rod of Asclepius, Helm of Radiance,
    Chronos'' Pendant, Jade Scepter, Spectral Armor, Erosion, Ethereal Staff, Eye
    of Providence, Alchemist Coat, Draconic Scale, Death Metal, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.36
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.6
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.47
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.7
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Genji''s Guard, Nimble Ring, Breastplate of Valor, Kinetic
    Cuirass, Death Metal, Amanita Charm, The Cosmic Horror, Oni Hunter''s Garb, Spear
    of the Magus, Shield of the Phoenix, Rod of Asclepius, Chronos'' Pendant, Helm
    of Radiance, Jade Scepter, Triton''s Conch, Spectral Armor, Bancroft''s Talon,
    Yogi''s Necklace, Ethereal Staff, Doom Orb, Bragi''s Harp, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.26
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.26
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.26
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.45
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.42
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Genji''s Guard, The Cosmic Horror, Nimble
    Ring, Kinetic Cuirass, Amanita Charm, Spear of the Magus, Breastplate of Valor,
    Shield of the Phoenix, Death Metal, Oni Hunter''s Garb, Chronos'' Pendant, Rod
    of Asclepius, Spectral Armor, Helm of Radiance, Chandra''s Grace, Jade Scepter,
    Screeching Gargoyle, Doom Orb, Erosion, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.24
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.32
    Spear of Desolation:
      total: 0.6
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.56
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.4
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Nimble Ring,
    Blood-Bound Book, Oni Hunter''s Garb, Lifebinder, The Cosmic Horror, Bancroft''s
    Talon, Breastplate of Valor, Spear of the Magus, Phoenix Feather, Erosion, Spectral
    Armor, Eye of Providence, Draconic Scale, Helm of Radiance, Jade Scepter.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.42
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.49
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.39
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Freya's Tears
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Spear of the Magus
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, The Cosmic Horror, Spear of the Magus,
    Genji''s Guard, Kinetic Cuirass, Nimble Ring, Amanita Charm, Screeching Gargoyle,
    Void Shield, Stone of Binding, Breastplate of Valor, Doom Orb, Oni Hunter''s Garb,
    Shield of the Phoenix, Void Stone, Rod of Asclepius, Helm of Radiance, Spectral
    Armor, Chronos'' Pendant, Jade Scepter, Obsidian Shard.'
  slot_scores:
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.29
    Spear of Desolation:
      total: 0.62
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.68
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.58
    Spear of the Magus:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.58
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Genji''s Guard, Kinetic
    Cuirass, Amanita Charm, Breastplate of Valor, The Cosmic Horror, Spear of the
    Magus, Oni Hunter''s Garb, Death Metal, Shield of the Phoenix, Bracer of The Abyss,
    Spectral Armor, Rod of Asclepius, Bragi''s Harp, Helm of Radiance, Chronos'' Pendant,
    Blood-Bound Book, Jade Scepter, Eye of Providence, Bancroft''s Talon, Erosion,
    Obsidian Shard.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.38
    Bragi's Harp:
      total: 0.5
      efficiency: 0.42
      win: 0.62
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.32
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.25
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Gluttonous
    Grimoire, Breastplate of Valor, Shield of the Phoenix, Kinetic Cuirass, Amanita
    Charm, Chronos'' Pendant, Nimble Ring, Chandra''s Grace, Screeching Gargoyle,
    Oni Hunter''s Garb, The Cosmic Horror, Gladiator''s Shield, Spear of the Magus,
    Gem of Focus, Spectral Armor, Totem of Death, Death Metal, Prophetic Cloak, Erosion,
    Rod of Asclepius, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.51
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.61
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.26
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Nimble Ring, Berserker''s Shield, Genji''s Guard, Kinetic Cuirass,
    Amanita Charm, Runeforged Hammer, Hydra''s Lament, Death Metal, The Cosmic Horror,
    Golden Blade, Spear of the Magus, Breastplate of Valor, Oni Hunter''s Garb, The
    Reaper, Lernaean Bow, Eye of the Storm, Shield of the Phoenix, Shield Splitter,
    Bragi''s Harp, Damaru, Pharaoh''s Curse, Avenging Blade, Rod of Asclepius, Helm
    of Radiance, Spectral Armor, Triton''s Conch, Chronos'' Pendant, Tekko-Kagi, Jade
    Scepter, Tyrfing, Riptalon, Erosion, Obsidian Shard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.24
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.41
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.32
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Gluttonous Grimoire, The
    Crusher, Jotunn''s Revenge, Nimble Ring, Genji''s Guard, Kinetic Cuirass, Amanita
    Charm, The Cosmic Horror, Berserker''s Shield, Death Metal, Spear of the Magus,
    Runeforged Hammer, Hydra''s Lament, Breastplate of Valor, Oni Hunter''s Garb,
    Shield of the Phoenix, Rod of Asclepius, The Reaper, Eye of the Storm, Helm of
    Radiance, Shield Splitter, Chronos'' Pendant, Golden Blade, Jade Scepter, Triton''s
    Conch, Spectral Armor, Avenging Blade, Damaru, Ethereal Staff, Erosion, Bragi''s
    Harp, Alchemist Coat, Pharaoh''s Curse, Eye of Providence, Blood-Bound Book, Obsidian
    Shard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.35
      fit: 0.27
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.48
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.39
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.7
      pick: 0.1
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Rod of Tahuti
  flex_slots:
  - The Cosmic Horror
  - Spear of Desolation
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita
    Charm, Genji''s Guard, Nimble Ring, The Cosmic Horror, Spear of the Magus, Breastplate
    of Valor, Shield of the Phoenix, Oni Hunter''s Garb, Rod of Asclepius, Obsidian
    Shard, Helm of Radiance, Chronos'' Pendant, Jade Scepter, Spectral Armor, Erosion,
    Ethereal Staff, Eye of Providence, Alchemist Coat, Draconic Scale, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.62
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.74
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.73
      pick: 0.16
      fit: 0.6
    The Cosmic Horror:
      total: 0.55
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.77
      win: 0.68
      pick: 0.45
      fit: 0.47
  starter: *id001
---
