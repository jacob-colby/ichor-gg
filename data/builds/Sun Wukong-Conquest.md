---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.59
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.35
    win_rate: 0.55
    alternates:
    - name: Mystical Mail
      pick_rate: 0.14
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.81
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.47
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.86
  - name: Soul Gem
    pick_rate: 0.08
    win_rate: 0.77
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.58
  - name: Sundering Echo
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Oracle Staff
      pick_rate: 0.04
      win_rate: 1.0
    - name: Dwarven Plate
      pick_rate: 0.04
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-01'
  god_win_rate: 0.5892857142857143
  god_matches_won: 99
  god_matches_played: 168
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Shifter's Shield
  - Spear of Desolation
  - Dwarven Plate
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Berserker''s Shield, Amanita Charm, Runeforged Hammer, Breastplate
    of Valor, Gluttonous Grimoire, Genji''s Guard, Kinetic Cuirass, Draconic Scale,
    The Crusher, Jotunn''s Revenge, Eye of Providence, Golden Blade, Oni Hunter''s
    Garb, Hydra''s Lament, Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Avenging
    Blade, Shield Splitter, Death Metal, Yogi''s Necklace, Spectral Armor, Shield
    of the Phoenix, Freya''s Tears, Shogun''s Ofuda, Erosion, Damaru, Rod of Asclepius,
    Dominance, Triton''s Conch, Leviathan''s Hide, Bragi''s Harp, Tyrfing, Jade Scepter,
    Midgardian Mail, Hide of the Nemean Lion, The Reaper, Wyrmskin Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.42
      win: 0.86
      pick: 0.08
      fit: 0.06
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.35
      fit: 0.45
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.81
      pick: 0.1
      fit: 0.16
    Dwarven Plate:
      total: 0.61
      efficiency: 0.35
      win: 1.0
      pick: 0.04
      fit: 0.25
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.77
      pick: 0.08
      fit: 0.26
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Spear of Desolation
  - Dwarven Plate
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Berserker''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, Draconic Scale, Breastplate of Valor, Genji''s Guard, Eye of
    Providence, Gluttonous Grimoire, Rod of Asclepius, Runeforged Hammer, Oni Hunter''s
    Garb, The Crusher, Jotunn''s Revenge, Golden Blade, Pharaoh''s Curse, The Reaper,
    Eye of the Storm, Shield Splitter, Chandra''s Grace, Hydra''s Lament, Freya''s
    Tears, Erosion, Phoenix Feather, Spectral Armor, Riptalon, Avenging Blade, Lernaean
    Bow, Yogi''s Necklace, Blood-Bound Book, Shogun''s Ofuda, Lifebinder, Bancroft''s
    Talon, Leviathan''s Hide, Death Metal, Midgardian Mail, Hide of the Nemean Lion,
    Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.42
      win: 0.86
      pick: 0.08
      fit: 0.05
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.81
      pick: 0.1
      fit: 0.14
    Dwarven Plate:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.04
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.84
    Soul Gem:
      total: 0.64
      efficiency: 0.59
      win: 0.77
      pick: 0.08
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Dwarven Plate
  - The Crusher
  - Soul Gem
  flex_slots:
  - Book of Thoth
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Spear of Desolation, Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Obsidian Shard, Berserker''s Shield, Avenging Blade, Breastplate
    of Valor, Genji''s Guard, Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Spear
    of the Magus, The Reaper, Eye of Providence, Oni Hunter''s Garb, The Cosmic Horror,
    Hydra''s Lament, Riptalon, Void Shield, Heartseeker, Golden Blade, Silverbranch
    Bow, Stone of Binding, Tekko-Kagi, Lernaean Bow, Screeching Gargoyle, Pharaoh''s
    Curse, Void Stone, Yogi''s Necklace, Eye of the Storm, Death Metal, Spectral Armor,
    Titan''s Bane, Shield Splitter, Freya''s Tears, Shield of the Phoenix, Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.42
      win: 0.86
      pick: 0.08
      fit: 0.04
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.62
      efficiency: 0.52
      win: 0.81
      pick: 0.1
      fit: 0.42
    Dwarven Plate:
      total: 0.6
      efficiency: 0.35
      win: 1.0
      pick: 0.04
      fit: 0.17
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.77
      pick: 0.08
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Spear of Desolation
  - Riptalon
  - Dwarven Plate
  - Soul Gem
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Berserker''s Shield, Golden Blade, Gluttonous Grimoire, Breastplate
    of Valor, Genji''s Guard, Amanita Charm, Riptalon, Pharaoh''s Curse, Kinetic Cuirass,
    The Crusher, Lernaean Bow, Runeforged Hammer, Eye of Providence, Tyrfing, Oni
    Hunter''s Garb, Jotunn''s Revenge, Silverbranch Bow, Shogun''s Ofuda, Hydra''s
    Lament, Yogi''s Necklace, Dominance, Bracer of The Abyss, Spectral Armor, Freya''s
    Tears, Bragi''s Harp, Shield of the Phoenix, Death Metal, Eros'' Bow, Avenging
    Blade, Eye of the Storm, Toxic Blade, Rod of Asclepius, Shield Splitter, Damaru,
    Erosion, Leviathan''s Hide, Jade Scepter, The Reaper.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.81
      pick: 0.1
      fit: 0.11
    Riptalon:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
    Dwarven Plate:
      total: 0.6
      efficiency: 0.35
      win: 1.0
      pick: 0.04
      fit: 0.16
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.77
      pick: 0.08
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Dwarven Plate
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Spear of Desolation, Breastplate
    of Valor, Genji''s Guard, Jotunn''s Revenge, Hydra''s Lament, Berserker''s Shield,
    Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix, Amanita Charm, Kinetic
    Cuirass, Chronos'' Pendant, Eye of Providence, The Crusher, Oni Hunter''s Garb,
    Runeforged Hammer, Chandra''s Grace, Screeching Gargoyle, Pharaoh''s Curse, Yogi''s
    Necklace, Gem of Focus, Gladiator''s Shield, Arondight, Rod of Asclepius, Golden
    Blade, Spectral Armor, Death Metal, Lernaean Bow, Jade Scepter, Spear of the Magus,
    Eye of the Storm, Helm of Radiance, Avenging Blade, Shogun''s Ofuda, Erosion,
    Shield Splitter, Leviathan''s Hide, Prophetic Cloak.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.42
      win: 0.86
      pick: 0.08
      fit: 0.1
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.52
      pick: 0.15
      fit: 0.44
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.07
      fit: 0.44
    Spear of Desolation:
      total: 0.63
      efficiency: 0.52
      win: 0.81
      pick: 0.1
      fit: 0.49
    Dwarven Plate:
      total: 0.6
      efficiency: 0.35
      win: 1.0
      pick: 0.04
      fit: 0.17
    Soul Gem:
      total: 0.65
      efficiency: 0.59
      win: 0.77
      pick: 0.08
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Runeforged Hammer,
    Gluttonous Grimoire, Kinetic Cuirass, The Crusher, Jotunn''s Revenge, Eye of Providence,
    Golden Blade, Oni Hunter''s Garb, Genji''s Guard, Hydra''s Lament, Eye of the
    Storm, Pharaoh''s Curse, Lernaean Bow, Avenging Blade, Shield Splitter, Death
    Metal, Yogi''s Necklace, Spectral Armor, Shield of the Phoenix, Breastplate of
    Valor, Shogun''s Ofuda, Erosion, Freya''s Tears, Damaru, Rod of Asclepius, Soul
    Gem, Dominance, Draconic Scale, Triton''s Conch, Leviathan''s Hide, Bragi''s Harp,
    Tyrfing, Jade Scepter, Midgardian Mail, Hide of the Nemean Lion, The Reaper, Wyrmskin
    Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
---
