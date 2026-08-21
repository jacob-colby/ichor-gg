---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.51
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.53
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.19
      win_rate: 0.56
    - name: Chronos' Pendant
      pick_rate: 0.07
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.65
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.57
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.58
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.51
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.41
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.72
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.85
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.47
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.73
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.69
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.31
    win_rate: 0.45
  - name: Bumba's Hammer
    pick_rate: 0.28
    win_rate: 0.66
  - name: Bluestone Brooch
    pick_rate: 0.1
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-21'
  god_win_rate: 0.537261698440208
  god_matches_won: 310
  god_matches_played: 577
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Jotunn''s
    Revenge, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Mantle Of
    Discord, Eye of the Storm, Stone of Binding, Gluttonous Grimoire, Erosion, Eye
    of Providence, Draconic Scale, Spectral Armor, The Crusher, Death Metal, Hydra''s
    Lament, Golden Blade, Leviathan''s Hide, Helm of Radiance, Pharaoh''s Curse, Magi''s
    Cloak, Soul Gem, Avenging Blade, Shogun''s Ofuda, Midgardian Mail, Screeching
    Gargoyle, Nimble Ring, Doublet of Binding, Heartseeker, Void Shield, Daybreak
    Gavel, Stampede, Spear of Desolation, Ethereal Staff.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.48
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.4
      fit: 0.53
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.53
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Rod of Tahuti, Shield of the Phoenix,
    Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield, Soul Gem, Ethereal Staff,
    Rod of Asclepius, The Reaper, Shield Splitter, Gluttonous Grimoire, Eye of the
    Storm, Phoenix Feather, Chandra''s Grace, Erosion, Yogi''s Necklace, Eye of Providence,
    Golden Blade, Spectral Armor, The Crusher, Death Metal, Mantle Of Discord, Stone
    of Binding, Hydra''s Lament, Draconic Scale, Avenging Blade, Leviathan''s Hide,
    Pharaoh''s Curse, Lifebinder, Riptalon, Glorious Pridwen, Blood-Bound Book, Helm
    of Radiance, Shogun''s Ofuda, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.76
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.19
      fit: 0.51
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.42
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge, Stone of Binding,
    Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, The Crusher, Berserker''s
    Shield, Soul Gem, Avenging Blade, Screeching Gargoyle, Void Shield, Spear of Desolation,
    Spear of the Magus, Heartseeker, Void Stone, Shield Splitter, The Reaper, Obsidian
    Shard, Shield of the Phoenix, Mantle Of Discord, Titan''s Bane, Death Metal, Eye
    of the Storm, Spectral Armor, Erosion, Hydra''s Lament, Eye of Providence, Tekko-Kagi,
    Helm of Radiance, Silverbranch Bow, Draconic Scale, Doom Orb, Nimble Ring, The
    Cosmic Horror, Leviathan''s Hide, Pharaoh''s Curse.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Nimble Ring, Golden Blade, Gluttonous Grimoire, Pharaoh''s
    Curse, Shogun''s Ofuda, Tyrfing, Shield Splitter, Shield of the Phoenix, Mantle
    Of Discord, Stone of Binding, Soul Gem, Riptalon, Lernaean Bow, Silverbranch Bow,
    Spectral Armor, The Crusher, Death Metal, Erosion, Helm of Radiance, Eye of Providence,
    Eye of the Storm, Hydra''s Lament, Toxic Blade, Draconic Scale, Leviathan''s Hide,
    Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Midgardian Mail,
    Spear of Desolation, Bragi''s Harp.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.33
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s Shield,
    Soul Gem, Spear of Desolation, Hydra''s Lament, Gluttonous Grimoire, Screeching
    Gargoyle, Shield Splitter, Mantle Of Discord, Stone of Binding, Prophetic Cloak,
    Helm of Radiance, Erosion, Spectral Armor, Death Metal, Nimble Ring, Eye of Providence,
    Draconic Scale, Chandra''s Grace, Eye of the Storm, Gladiator''s Shield, Arondight,
    Gem of Focus, Leviathan''s Hide, The Crusher, Pharaoh''s Curse, Chronos'' Pendant,
    Magi''s Cloak, Ethereal Staff, Rod of Asclepius, Spear of the Magus, Eye of Erebus,
    Totem of Death.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.27
      fit: 0.45
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.53
      pick: 0.22
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.69
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.6
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, The
    Crusher, Shield Splitter, Golden Blade, Soul Gem, Death Metal, Eye of the Storm,
    Shield of the Phoenix, Hydra''s Lament, Mantle Of Discord, Stone of Binding, Heartseeker,
    Nimble Ring, The Reaper, Pharaoh''s Curse, Lernaean Bow, Spectral Armor, Erosion,
    Spear of Desolation, Spear of the Magus, Tyrfing, Eye of Providence, Shogun''s
    Ofuda, Tekko-Kagi, Avenging Blade, Helm of Radiance, Draconic Scale, Titan''s
    Bane, Obsidian Shard, Leviathan''s Hide, Magi''s Cloak, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.19
      fit: 0.43
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Berserker''s Shield,
    Soul Gem, Death Metal, The Crusher, Shield Splitter, Spear of Desolation, Spear
    of the Magus, Helm of Radiance, Nimble Ring, Obsidian Shard, Shield of the Phoenix,
    Mantle Of Discord, Stone of Binding, Eye of the Storm, Ethereal Staff, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Spectral Armor, Erosion, The Reaper, Eye
    of Providence, Draconic Scale, Golden Blade, Jade Scepter, Leviathan''s Hide,
    Doom Orb, The Cosmic Horror, Pharaoh''s Curse, Wish-Granting Pearl, Avenging Blade,
    Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.49
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.19
      fit: 0.38
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Jotunn''s
    Revenge, Berserker''s Shield, Freya''s Tears, Shield Splitter, Shield of the Phoenix,
    Mantle Of Discord, Eye of the Storm, Stone of Binding, Gluttonous Grimoire, Erosion,
    Eye of Providence, Draconic Scale, Spectral Armor, The Crusher, Death Metal, Hydra''s
    Lament, Golden Blade, Leviathan''s Hide, Helm of Radiance, Pharaoh''s Curse, Magi''s
    Cloak, Soul Gem, Avenging Blade, Shogun''s Ofuda, Midgardian Mail, Screeching
    Gargoyle, Nimble Ring, Doublet of Binding, Heartseeker, Void Shield, Daybreak
    Gavel, Stampede, Spear of Desolation, Ethereal Staff.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.63
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.85
      pick: 0.13
      fit: 0.48
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.53
  starter: *id001
---
