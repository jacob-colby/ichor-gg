---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.39
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.35
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.12
      win_rate: 0.6
    - name: Chronos' Pendant
      pick_rate: 0.11
      win_rate: 0.44
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.36
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.44
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.63
  - name: Soul Gem
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.29
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.83
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.44
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.38
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.33
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Shield
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.62
  - name: Archmage's Gem
    pick_rate: 0.11
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-14'
  god_win_rate: 0.4880952380952381
  god_matches_won: 41
  god_matches_played: 84
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Kinetic Cuirass, The Crusher,
    Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge, Golden Blade, Nimble Ring,
    Eye of the Storm, Oni Hunter''s Garb, Pharaoh''s Curse, Hydra''s Lament, Shield
    Splitter, Shield of the Phoenix, Avenging Blade, Spectral Armor, Lernaean Bow,
    Freya''s Tears, Erosion, Breastplate of Valor, Eye of Providence, Death Metal,
    Shogun''s Ofuda, Draconic Scale, Damaru, Leviathan''s Hide, Midgardian Mail, Tyrfing,
    Triton''s Conch, The Reaper, Rod of Asclepius, Yogi''s Necklace, Wyrmskin Hide,
    Bragi''s Harp, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.55
    Gladiator's Shield:
      total: 0.5
      efficiency: 0.41
      win: 0.63
      pick: 0.14
      fit: 0.47
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.56
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.44
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.51
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.12
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Gladiator's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Berserker''s Shield, Gluttonous Grimoire, The Crusher, Rod of Asclepius, Oni Hunter''s
    Garb, Jotunn''s Revenge, The Reaper, Chandra''s Grace, Eye of the Storm, Golden
    Blade, Pharaoh''s Curse, Erosion, Nimble Ring, Shield Splitter, Phoenix Feather,
    Freya''s Tears, Eye of Providence, Spectral Armor, Draconic Scale, Riptalon, Breastplate
    of Valor, Hydra''s Lament, Shogun''s Ofuda, Avenging Blade, Leviathan''s Hide,
    Midgardian Mail, Blood-Bound Book, Lifebinder, Lernaean Bow, Bancroft''s Talon,
    Death Metal, Ancile, Damaru.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.64
    Gladiator's Shield:
      total: 0.51
      efficiency: 0.41
      win: 0.63
      pick: 0.14
      fit: 0.51
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.53
    Obsidian Shard:
      total: 0.51
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.1
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.84
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.23
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Runeforged Hammer, The Crusher, Gluttonous Grimoire, Jotunn''s Revenge,
    Berserker''s Shield, Avenging Blade, Kinetic Cuirass, Amanita Charm, The Reaper,
    The Cosmic Horror, Nimble Ring, Spear of the Magus, Void Shield, Riptalon, Stone
    of Binding, Screeching Gargoyle, Oni Hunter''s Garb, Tekko-Kagi, Silverbranch
    Bow, Golden Blade, Void Stone, Hydra''s Lament, Breastplate of Valor, Heartseeker,
    Pharaoh''s Curse, Eye of the Storm, Toxic Blade, Spectral Armor, Shield of the
    Phoenix, Freya''s Tears, Titan''s Bane, Shield Splitter, Lernaean Bow, Death Metal,
    Erosion, Pendulum Blade, Spear of Desolation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.44
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.44
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.44
      pick: 0.2
      fit: 0.39
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.39
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.23
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Gladiator's Shield
  - Nimble Ring
  - Runeforged Hammer
  - Obsidian Shard
  flex_slots:
  - Gladiator's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Nimble Ring, Golden Blade, Gluttonous
    Grimoire, Kinetic Cuirass, Riptalon, The Crusher, Amanita Charm, Pharaoh''s Curse,
    Tyrfing, Jotunn''s Revenge, Silverbranch Bow, Lernaean Bow, Oni Hunter''s Garb,
    Shogun''s Ofuda, Breastplate of Valor, Toxic Blade, Spectral Armor, Hydra''s Lament,
    Freya''s Tears, Shield of the Phoenix, Eye of the Storm, Erosion, Eros'' Bow,
    Shield Splitter, Bragi''s Harp, Leviathan''s Hide, Eye of Providence, Death Metal,
    Avenging Blade, Bracer of The Abyss, Dominance, Midgardian Mail, The Reaper, Yogi''s
    Necklace, Damaru.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.45
    Gladiator's Shield:
      total: 0.49
      efficiency: 0.41
      win: 0.63
      pick: 0.14
      fit: 0.34
    Nimble Ring:
      total: 0.49
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.36
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.36
    Obsidian Shard:
      total: 0.51
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.08
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Runeforged Hammer
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Runeforged Hammer,
    Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix, Freya''s Tears,
    Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, Kinetic Cuirass, Nimble
    Ring, Amanita Charm, Chronos'' Pendant, The Crusher, Chandra''s Grace, Screeching
    Gargoyle, Oni Hunter''s Garb, Pharaoh''s Curse, Gem of Focus, Spectral Armor,
    Golden Blade, Totem of Death, Arondight, Erosion, Rod of Asclepius, Death Metal,
    Prophetic Cloak, Eye of the Storm, The Cosmic Horror, Eye of Providence, Leviathan''s
    Hide, Shogun''s Ofuda, Helm of Radiance, Midgardian Mail, Spear of the Magus,
    Jade Scepter, Spear of Desolation.'
  slot_scores:
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.64
      win: 0.44
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.64
      win: 0.44
      pick: 0.0
      fit: 0.49
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.63
      pick: 0.14
      fit: 0.67
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.34
    Obsidian Shard:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.28
      fit: 0.15
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.23
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
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, The Crusher, Amanita
    Charm, Gluttonous Grimoire, Jotunn''s Revenge, Runeforged Hammer, Golden Blade,
    Nimble Ring, Eye of the Storm, Oni Hunter''s Garb, Pharaoh''s Curse, Hydra''s
    Lament, Shield Splitter, Shield of the Phoenix, Avenging Blade, Spectral Armor,
    Lernaean Bow, Freya''s Tears, Erosion, Breastplate of Valor, Eye of Providence,
    Death Metal, Shogun''s Ofuda, Draconic Scale, Damaru, Leviathan''s Hide, Midgardian
    Mail, Tyrfing, Triton''s Conch, The Reaper, Rod of Asclepius, Yogi''s Necklace,
    Wyrmskin Hide, Bragi''s Harp, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.64
      win: 0.44
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.56
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.44
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.45
  starter: *id001
---
