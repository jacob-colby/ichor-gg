---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.02
  aspect_win_rate: 1.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.62
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.13
      win_rate: 0.43
    - name: Eye of Erebus
      pick_rate: 0.13
      win_rate: 0.71
  - name: Prophetic Cloak
    pick_rate: 0.23
    win_rate: 0.58
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.15
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.71
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.64
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.2
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.8
  - name: Gladiator's Shield
    pick_rate: 0.2
    win_rate: 0.6
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.18
      win_rate: 0.67
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Brawler's Beat Stick
      pick_rate: 0.08
      win_rate: 0.75
    - name: Ethereal Staff
      pick_rate: 0.08
      win_rate: 0.75
  - name: Soul Reliquary
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.1
      win_rate: 0.67
    - name: Flaming Pearl
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.44
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.54
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-08-13'
  god_win_rate: 0.5769230769230769
  god_matches_won: 30
  god_matches_played: 52
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
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Jotunn''s Revenge, Pharaoh''s Curse, Freya''s Tears, The Crusher, Oni Hunter''s
    Garb, Golden Blade, Shield of the Phoenix, Shield Splitter, Hydra''s Lament, Lernaean
    Bow, Shogun''s Ofuda, Runeforged Hammer, Erosion, Eye of Providence, Spectral
    Armor, Eye of the Storm, Soul Gem, Draconic Scale, Leviathan''s Hide, Death Metal,
    Mantle Of Discord, Helm of Radiance, Midgardian Mail, Stone of Binding, Damaru,
    Avenging Blade, Bracer of The Abyss, Dominance, Riptalon, Yogi''s Necklace, Tyrfing,
    Bragi''s Harp, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.26
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.16
      fit: 0.26
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.48
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Soul Gem,
    Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, Rod of Asclepius, Riptalon,
    Pharaoh''s Curse, The Crusher, Golden Blade, Chandra''s Grace, Oni Hunter''s Garb,
    Freya''s Tears, Runeforged Hammer, The Reaper, Hydra''s Lament, Shogun''s Ofuda,
    Lernaean Bow, Blood-Bound Book, Bancroft''s Talon, Phoenix Feather, Eye of the
    Storm, Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Draconic Scale,
    Lifebinder, Leviathan''s Hide, Death Metal, Midgardian Mail, Avenging Blade, Yogi''s
    Necklace, Dominance, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.23
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.49
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.16
      fit: 0.23
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.56
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Kinetic Cuirass, Soul Gem, Amanita Charm, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Void Shield, Riptalon, Freya''s Tears, Pharaoh''s Curse,
    Spear of the Magus, Oni Hunter''s Garb, The Cosmic Horror, Silverbranch Bow, Hydra''s
    Lament, Void Stone, Golden Blade, Shield of the Phoenix, Lernaean Bow, Runeforged
    Hammer, The Reaper, Shield Splitter, Shogun''s Ofuda, Spectral Armor, Spear of
    Desolation, Erosion, Tekko-Kagi, Obsidian Shard, Eye of Providence, Eye of the
    Storm, Heartseeker, Draconic Scale, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.2
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.37
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.16
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Gluttonous Grimoire
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The Crusher, Freya''s
    Tears, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda, Shield of
    the Phoenix, Silverbranch Bow, Hydra''s Lament, Tyrfing, Runeforged Hammer, Spectral
    Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of The Abyss, Draconic
    Scale, Eye of the Storm, Helm of Radiance, Leviathan''s Hide, Midgardian Mail,
    Mantle Of Discord, Yogi''s Necklace, Death Metal, Stone of Binding, Eros'' Bow,
    Dominance, Spear of the Magus, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.2
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.16
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.34
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Jotunn''s Revenge,
    Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Amanita Charm,
    Shield of the Phoenix, Hydra''s Lament, Pharaoh''s Curse, Oni Hunter''s Garb,
    The Crusher, Chronos'' Pendant, Screeching Gargoyle, Spear of Desolation, Shogun''s
    Ofuda, Chandra''s Grace, Spectral Armor, Erosion, Golden Blade, Lernaean Bow,
    Eye of Providence, Runeforged Hammer, Helm of Radiance, Shield Splitter, Draconic
    Scale, Gem of Focus, Bracer of The Abyss, Leviathan''s Hide, Spear of the Magus,
    Rod of Asclepius, Death Metal, Eye of the Storm, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.41
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.66
      efficiency: 0.66
      win: 0.8
      pick: 0.16
      fit: 0.41
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Freya''s
    Tears, Soul Gem, Oni Hunter''s Garb, Runeforged Hammer, Shield Splitter, Pharaoh''s
    Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Erosion,
    Spectral Armor, Death Metal, Eye of Providence, Spear of the Magus, Shogun''s
    Ofuda, The Reaper, Draconic Scale, Damaru, Avenging Blade, The Cosmic Horror,
    Riptalon, Leviathan''s Hide, Helm of Radiance, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Tekko-Kagi, Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.23
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.16
      fit: 0.23
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - The Crusher
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Amanita Charm, Soul Gem,
    Freya''s Tears, Pharaoh''s Curse, Oni Hunter''s Garb, Spear of the Magus, Hydra''s
    Lament, Death Metal, The Cosmic Horror, Golden Blade, Lernaean Bow, Runeforged
    Hammer, Helm of Radiance, Shield of the Phoenix, Shield Splitter, Bracer of The
    Abyss, Spectral Armor, Shogun''s Ofuda, Rod of Asclepius, Spear of Desolation,
    Erosion, Riptalon, Eye of the Storm, Bragi''s Harp, Jade Scepter, Obsidian Shard,
    Eye of Providence, Chronos'' Pendant, Silverbranch Bow, Draconic Scale, Blood-Bound
    Book, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.2
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.16
      fit: 0.2
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Gluttonous Grimoire, Jotunn''s Revenge, Pharaoh''s Curse, Freya''s Tears, The
    Crusher, Oni Hunter''s Garb, Golden Blade, Shield of the Phoenix, Shield Splitter,
    Hydra''s Lament, Lernaean Bow, Shogun''s Ofuda, Runeforged Hammer, Erosion, Eye
    of Providence, Spectral Armor, Eye of the Storm, Soul Gem, Draconic Scale, Leviathan''s
    Hide, Death Metal, Mantle Of Discord, Helm of Radiance, Midgardian Mail, Stone
    of Binding, Damaru, Avenging Blade, Bracer of The Abyss, Dominance, Riptalon,
    Yogi''s Necklace, Tyrfing, Bragi''s Harp, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.34
      fit: 0.26
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.48
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.48
  starter: *id001
---
