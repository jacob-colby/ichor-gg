---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.3
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.4
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.15
      win_rate: 0.33
    - name: Gem of Focus
      pick_rate: 0.12
      win_rate: 0.4
  - name: Mercury's Talaria
    pick_rate: 0.12
    win_rate: 0.4
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.4
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.43
    alternates:
    - name: Soul Gem
      pick_rate: 0.17
      win_rate: 0.43
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.4
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.25
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.25
  - name: Evil Eye
    pick_rate: 0.12
    win_rate: 0.25
    alternates:
    - name: Necronomicon
      pick_rate: 0.09
      win_rate: 0.67
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Contagion
      pick_rate: 0.08
      win_rate: 1.0
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.32
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.7
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-13'
  god_win_rate: 0.5365853658536586
  god_matches_won: 22
  god_matches_played: 41
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Jotunn''s Revenge, The Crusher, Golden Blade, Runeforged Hammer, Oni Hunter''s
    Garb, Pharaoh''s Curse, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Shield
    Splitter, Shield of the Phoenix, Spectral Armor, Avenging Blade, Shogun''s Ofuda,
    Death Metal, Freya''s Tears, Erosion, Eye of Providence, Damaru, Draconic Scale,
    Leviathan''s Hide, Yogi''s Necklace, Midgardian Mail, Rod of Asclepius, Bragi''s
    Harp, Dominance, Triton''s Conch, Tyrfing, Jade Scepter, Helm of Radiance, The
    Reaper, Wyrmskin Hide.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.3
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.43
      pick: 0.26
      fit: 0.17
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.17
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.59
      win: 0.43
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.42
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Gluttonous Grimoire, Rod of Asclepius, The Crusher, Jotunn''s Revenge, Oni Hunter''s
    Garb, Pharaoh''s Curse, Runeforged Hammer, Golden Blade, The Reaper, Eye of the
    Storm, Chandra''s Grace, Riptalon, Shield Splitter, Erosion, Phoenix Feather,
    Freya''s Tears, Spectral Armor, Eye of Providence, Blood-Bound Book, Hydra''s
    Lament, Shogun''s Ofuda, Bancroft''s Talon, Draconic Scale, Lernaean Bow, Leviathan''s
    Hide, Avenging Blade, Lifebinder, Midgardian Mail, Death Metal, Yogi''s Necklace,
    Damaru, Helm of Radiance.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.31
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.2
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.43
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Obsidian Shard
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
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Heartseeker,
    Berserker''s Shield, Avenging Blade, Kinetic Cuirass, Spear of the Magus, Amanita
    Charm, The Cosmic Horror, Riptalon, The Reaper, Runeforged Hammer, Void Shield,
    Silverbranch Bow, Stone of Binding, Oni Hunter''s Garb, Golden Blade, Hydra''s
    Lament, Screeching Gargoyle, Tekko-Kagi, Pharaoh''s Curse, Void Stone, Lernaean
    Bow, Eye of the Storm, Titan''s Bane, Spectral Armor, Shield of the Phoenix, Freya''s
    Tears, Death Metal, Shield Splitter, Toxic Blade, Shogun''s Ofuda, Damaru, The
    World Stone.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.24
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.12
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.46
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Gluttonous Grimoire
  - Riptalon
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Golden Blade, Riptalon, Pharaoh''s
    Curse, Kinetic Cuirass, Amanita Charm, The Crusher, Jotunn''s Revenge, Lernaean
    Bow, Silverbranch Bow, Tyrfing, Shogun''s Ofuda, Oni Hunter''s Garb, Runeforged
    Hammer, Hydra''s Lament, Bracer of The Abyss, Spectral Armor, Shield of the Phoenix,
    Freya''s Tears, Eros'' Bow, Toxic Blade, Dominance, Bragi''s Harp, Death Metal,
    Yogi''s Necklace, Eye of the Storm, Erosion, Nimble Ring, Shield Splitter, Rod
    of Asclepius, Leviathan''s Hide, Spear of the Magus, Damaru, Blood-Bound Book,
    Eye of Providence.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.23
    Golden Blade:
      total: 0.48
      efficiency: 0.54
      win: 0.43
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.11
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.47
      efficiency: 0.56
      win: 0.43
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    Berserker''s Shield, Hydra''s Lament, Shield of the Phoenix, Freya''s Tears, Kinetic
    Cuirass, Amanita Charm, The Crusher, Chandra''s Grace, Oni Hunter''s Garb, Screeching
    Gargoyle, Pharaoh''s Curse, Gladiator''s Shield, Runeforged Hammer, Golden Blade,
    Spectral Armor, Gem of Focus, Rod of Asclepius, Arondight, Death Metal, Spear
    of the Magus, Lernaean Bow, Helm of Radiance, Jade Scepter, Shogun''s Ofuda, Erosion,
    Yogi''s Necklace, Prophetic Cloak, The Cosmic Horror, Eye of the Storm, Chronos''
    Pendant, Bracer of The Abyss, Leviathan''s Hide, Eye of Providence.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.25
      fit: 0.24
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.43
      pick: 0.26
      fit: 0.44
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.44
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.49
    Soul Gem:
      total: 0.5
      efficiency: 0.59
      win: 0.43
      pick: 0.26
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Golden Blade
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Jotunn''s Revenge, The Crusher, Golden Blade, Runeforged Hammer,
    Oni Hunter''s Garb, Pharaoh''s Curse, Eye of the Storm, Hydra''s Lament, Lernaean
    Bow, Shield Splitter, Shield of the Phoenix, Spectral Armor, Avenging Blade, Shogun''s
    Ofuda, Death Metal, Freya''s Tears, Erosion, Eye of Providence, Damaru, Draconic
    Scale, Leviathan''s Hide, Yogi''s Necklace, Midgardian Mail, Rod of Asclepius,
    Bragi''s Harp, Dominance, Triton''s Conch, Tyrfing, Jade Scepter, Helm of Radiance,
    The Reaper, Wyrmskin Hide.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.54
      win: 0.43
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.43
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.59
      win: 0.43
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.66
      win: 0.43
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.48
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.42
  starter: *id001
---
