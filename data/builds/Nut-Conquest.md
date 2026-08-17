---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.47
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.36
    win_rate: 0.56
    alternates:
    - name: Tyrfing
      pick_rate: 0.36
      win_rate: 0.43
    - name: Book of Thoth
      pick_rate: 0.06
      win_rate: 0.6
  - name: Bragi's Harp
    pick_rate: 0.26
    win_rate: 0.44
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.18
      win_rate: 0.61
    - name: Spear of Desolation
      pick_rate: 0.07
      win_rate: 0.54
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.49
    alternates:
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.58
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.58
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.56
    - name: The Executioner
      pick_rate: 0.11
      win_rate: 0.53
  - name: The Executioner
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.68
  - name: Evil Eye
    pick_rate: 0.05
    win_rate: 0.4
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.05
      win_rate: 0.7
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.25
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-08-17'
  god_win_rate: 0.49271137026239065
  god_matches_won: 169
  god_matches_played: 343
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-17'
  god_matches_analyzed: 7467
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Transcendence
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Transcendence
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Berserker''s
    Shield, Riptalon, The Cosmic Horror, Genji''s Guard, Spear of the Magus, Lernaean
    Bow, Hydra''s Lament, Death Metal, The Reaper, Silverbranch Bow, Golden Blade,
    Bracer of The Abyss, Tekko-Kagi, Breastplate of Valor, Chronos'' Pendant, Blood-Bound
    Book, Runeforged Hammer, Pharaoh''s Curse, Bancroft''s Talon, Dominance, Helm
    of Radiance, Damaru, Kinetic Cuirass, Freya''s Tears, Rod of Asclepius, Amanita
    Charm, Doom Orb, Toxic Blade, The World Stone, Eye of Providence, Gem of Focus.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.6
      pick: 0.06
      fit: 0.19
    Transcendence:
      total: 0.44
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.16
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.36
      fit: 0.48
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.49
      pick: 0.2
      fit: 0.38
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.16
      fit: 0.68
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Jotunn''s Revenge, Gluttonous Grimoire, The Crusher, Genji''s Guard, Hydra''s
    Lament, Death Metal, Berserker''s Shield, The Cosmic Horror, Spear of the Magus,
    Lernaean Bow, Breastplate of Valor, Riptalon, Golden Blade, The Reaper, Bancroft''s
    Talon, Bracer of The Abyss, Runeforged Hammer, Chronos'' Pendant, Dominance, Tekko-Kagi,
    Blood-Bound Book, Silverbranch Bow, Damaru, Oni Hunter''s Garb, Helm of Radiance,
    Doom Orb, Transcendence, The World Stone, Rod of Asclepius, Heartseeker, Kinetic
    Cuirass, Pharaoh''s Curse, Freya''s Tears, Amanita Charm.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.49
      win: 0.6
      pick: 0.06
      fit: 0.28
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.46
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.49
      pick: 0.2
      fit: 0.42
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.16
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Transcendence
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Jotunn''s Revenge, Nimble Ring, The Crusher, Genji''s
    Guard, Riptalon, The Cosmic Horror, Berserker''s Shield, Spear of the Magus, Hydra''s
    Lament, The Reaper, Silverbranch Bow, Breastplate of Valor, Lernaean Bow, Tekko-Kagi,
    Death Metal, Golden Blade, Chronos'' Pendant, Bracer of The Abyss, Runeforged
    Hammer, Freya''s Tears, Blood-Bound Book, Pendulum Blade, Damaru, Pharaoh''s Curse,
    Kinetic Cuirass, Shield of the Phoenix, Doom Orb, Bancroft''s Talon, Amanita Charm,
    The World Stone, Dominance, Heartseeker, Gem of Focus, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.6
      pick: 0.06
      fit: 0.16
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.56
    Transcendence:
      total: 0.44
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.16
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.36
      fit: 0.56
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.49
      pick: 0.2
      fit: 0.4
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.16
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Nimble Ring, Berserker''s Shield,
    Shield of the Phoenix, Riptalon, Rod of Asclepius, The Crusher, Kinetic Cuirass,
    The Reaper, Genji''s Guard, Jotunn''s Revenge, Blood-Bound Book, Chandra''s Grace,
    Bancroft''s Talon, Pharaoh''s Curse, Oni Hunter''s Garb, Breastplate of Valor,
    Freya''s Tears, Golden Blade, Runeforged Hammer, Lifebinder, The Cosmic Horror,
    Phoenix Feather, Spectral Armor, Spear of the Magus, Shogun''s Ofuda, Hydra''s
    Lament, Erosion, Lernaean Bow, Shifter''s Shield, Death Metal, Eye of Providence,
    Helm of Radiance, Eye of the Storm, Umbral Link, Shield Splitter, Silverbranch
    Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.17
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.58
      pick: 0.16
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
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
    for this god: Gluttonous Grimoire, The Crusher, Nimble Ring, Jotunn''s Revenge,
    Riptalon, The Cosmic Horror, Spear of the Magus, The Reaper, Silverbranch Bow,
    Berserker''s Shield, Tekko-Kagi, Genji''s Guard, Avenging Blade, Screeching Gargoyle,
    Hydra''s Lament, Lernaean Bow, Death Metal, Golden Blade, Breastplate of Valor,
    Doom Orb, Bracer of The Abyss, The World Stone, Toxic Blade, Heartseeker, Chronos''
    Pendant, Blood-Bound Book, Runeforged Hammer, Dreamer''s Idol, Stone of Binding,
    Pendulum Blade, Titan''s Bane, Pharaoh''s Curse, Bancroft''s Talon, Kinetic Cuirass,
    Void Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.6
      pick: 0.06
      fit: 0.16
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.36
      fit: 0.57
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.49
      pick: 0.2
      fit: 0.49
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.16
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Nimble Ring
  - Spear of Desolation
  - Riptalon
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Nimble Ring, Gluttonous Grimoire, Riptalon, The Crusher, Jotunn''s Revenge,
    Berserker''s Shield, Silverbranch Bow, Golden Blade, Genji''s Guard, The Cosmic
    Horror, Spear of the Magus, Lernaean Bow, Hydra''s Lament, Death Metal, Bracer
    of The Abyss, The Reaper, Breastplate of Valor, Toxic Blade, Tekko-Kagi, Pharaoh''s
    Curse, Chronos'' Pendant, Blood-Bound Book, Runeforged Hammer, Kinetic Cuirass,
    Bancroft''s Talon, Dominance, Amanita Charm, Damaru, Freya''s Tears, Helm of Radiance,
    Eye of Providence, Rod of Asclepius, Oni Hunter''s Garb, Shogun''s Ofuda, Shield
    of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.48
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.36
      fit: 0.39
    Riptalon:
      total: 0.52
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.49
      pick: 0.2
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  flex_slots:
  - The Crusher
  - Hydra's Lament
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Genji''s
    Guard, Gluttonous Grimoire, The Crusher, Hydra''s Lament, Breastplate of Valor,
    Berserker''s Shield, Chronos'' Pendant, Riptalon, Freya''s Tears, Shield of the
    Phoenix, The Cosmic Horror, Lernaean Bow, Spear of the Magus, Silverbranch Bow,
    Screeching Gargoyle, Gem of Focus, Chandra''s Grace, The Reaper, Golden Blade,
    Pendulum Blade, Totem of Death, Arondight, Death Metal, Bracer of The Abyss, Tekko-Kagi,
    Pharaoh''s Curse, Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Blood-Bound
    Book, Eye of Providence, Oni Hunter''s Garb, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.36
      fit: 0.6
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.36
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.16
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - The Cosmic Horror
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, Gluttonous Grimoire, The Crusher, Jotunn''s
    Revenge, Berserker''s Shield, Riptalon, The Cosmic Horror, Genji''s Guard, Spear
    of the Magus, Lernaean Bow, Hydra''s Lament, Death Metal, The Reaper, Silverbranch
    Bow, Golden Blade, Bracer of The Abyss, Tekko-Kagi, Breastplate of Valor, Chronos''
    Pendant, Blood-Bound Book, Runeforged Hammer, Pharaoh''s Curse, Bancroft''s Talon,
    Dominance, Helm of Radiance, Damaru, Kinetic Cuirass, Freya''s Tears, Rod of Asclepius,
    Amanita Charm, Doom Orb, Toxic Blade, The World Stone, Eye of Providence, Gem
    of Focus.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.55
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.58
      win: 0.52
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.52
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.49
      pick: 0.2
      fit: 0.38
  starter: *id001
---
