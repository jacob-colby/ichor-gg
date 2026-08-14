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
  - Gluttonous Grimoire
  - Obsidian Shard
  flex_slots:
  - Gluttonous Grimoire
  - Kinetic Cuirass
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
    this god: Runeforged Hammer, Berserker''s Shield, Gluttonous Grimoire, Kinetic
    Cuirass, Amanita Charm, Jotunn''s Revenge, The Crusher, Golden Blade, Oni Hunter''s
    Garb, Pharaoh''s Curse, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Shield
    Splitter, Breastplate of Valor, Shield of the Phoenix, Spectral Armor, Avenging
    Blade, Shogun''s Ofuda, Death Metal, Freya''s Tears, Erosion, Eye of Providence,
    Damaru, Draconic Scale, Leviathan''s Hide, Yogi''s Necklace, Midgardian Mail,
    Rod of Asclepius, Bragi''s Harp, Dominance, Triton''s Conch, Tyrfing, Jade Scepter,
    Helm of Radiance, The Reaper, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
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
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.42
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.67
      pick: 0.28
      fit: 0.12
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Gladiator's Shield
  - Runeforged Hammer
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Gladiator's Shield
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Berserker''s Shield, Shield of the
    Phoenix, Kinetic Cuirass, Gluttonous Grimoire, Rod of Asclepius, The Crusher,
    Jotunn''s Revenge, Oni Hunter''s Garb, Pharaoh''s Curse, Golden Blade, The Reaper,
    Eye of the Storm, Chandra''s Grace, Riptalon, Shield Splitter, Erosion, Breastplate
    of Valor, Phoenix Feather, Freya''s Tears, Spectral Armor, Eye of Providence,
    Blood-Bound Book, Hydra''s Lament, Shogun''s Ofuda, Bancroft''s Talon, Draconic
    Scale, Lernaean Bow, Leviathan''s Hide, Avenging Blade, Lifebinder, Midgardian
    Mail, Death Metal, Yogi''s Necklace, Damaru, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.48
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
      total: 0.52
      efficiency: 0.54
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
      efficiency: 0.59
      win: 0.5
      pick: 0.23
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gladiator's Shield
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Jotunn's Revenge
  - Gladiator's Shield
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Runeforged Hammer, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge,
    Berserker''s Shield, Avenging Blade, Kinetic Cuirass, Spear of the Magus, Amanita
    Charm, The Cosmic Horror, Riptalon, The Reaper, Void Shield, Silverbranch Bow,
    Stone of Binding, Oni Hunter''s Garb, Heartseeker, Golden Blade, Hydra''s Lament,
    Screeching Gargoyle, Tekko-Kagi, Breastplate of Valor, Pharaoh''s Curse, Void
    Stone, Lernaean Bow, Eye of the Storm, Titan''s Bane, Spectral Armor, Shield of
    the Phoenix, Freya''s Tears, Death Metal, Shield Splitter, Toxic Blade, Shogun''s
    Ofuda, Damaru, The World Stone, Spear of Desolation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.56
    Gladiator's Shield:
      total: 0.49
      efficiency: 0.41
      win: 0.63
      pick: 0.14
      fit: 0.36
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.63
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.28
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Riptalon
  - Obsidian Shard
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Gluttonous Grimoire, Golden
    Blade, Riptalon, Pharaoh''s Curse, Kinetic Cuirass, Amanita Charm, The Crusher,
    Jotunn''s Revenge, Lernaean Bow, Silverbranch Bow, Tyrfing, Shogun''s Ofuda, Oni
    Hunter''s Garb, Breastplate of Valor, Hydra''s Lament, Bracer of The Abyss, Spectral
    Armor, Shield of the Phoenix, Freya''s Tears, Eros'' Bow, Toxic Blade, Dominance,
    Bragi''s Harp, Death Metal, Yogi''s Necklace, Eye of the Storm, Erosion, Nimble
    Ring, Shield Splitter, Rod of Asclepius, Leviathan''s Hide, Spear of the Magus,
    Damaru, Blood-Bound Book, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.54
      win: 0.44
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.12
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.47
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.52
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Runeforged Hammer,
    Jotunn''s Revenge, Breastplate of Valor, Gluttonous Grimoire, Berserker''s Shield,
    Hydra''s Lament, Shield of the Phoenix, Freya''s Tears, Kinetic Cuirass, Chronos''
    Pendant, Amanita Charm, The Crusher, Chandra''s Grace, Oni Hunter''s Garb, Screeching
    Gargoyle, Pharaoh''s Curse, Gem of Focus, Golden Blade, Spectral Armor, Rod of
    Asclepius, Arondight, Death Metal, Spear of the Magus, Lernaean Bow, Helm of Radiance,
    Jade Scepter, Shogun''s Ofuda, Erosion, Yogi''s Necklace, Prophetic Cloak, The
    Cosmic Horror, Eye of the Storm, Bracer of The Abyss, Leviathan''s Hide, Eye of
    Providence, Spear of Desolation.'
  slot_scores:
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.49
    Gladiator's Shield:
      total: 0.53
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
      total: 0.53
      efficiency: 0.54
      win: 0.67
      pick: 0.28
      fit: 0.15
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.23
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
    Bow, Shield Splitter, Breastplate of Valor, Shield of the Phoenix, Spectral Armor,
    Avenging Blade, Shogun''s Ofuda, Death Metal, Freya''s Tears, Erosion, Eye of
    Providence, Damaru, Draconic Scale, Leviathan''s Hide, Yogi''s Necklace, Midgardian
    Mail, Rod of Asclepius, Bragi''s Harp, Dominance, Triton''s Conch, Tyrfing, Jade
    Scepter, Helm of Radiance, The Reaper, Wyrmskin Hide.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.54
      win: 0.44
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.59
      win: 0.44
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.48
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.42
  starter: *id001
---
