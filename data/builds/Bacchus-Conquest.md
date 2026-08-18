---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.62
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.22
    win_rate: 0.54
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.59
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.69
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.47
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.11
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.55
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.58
  - name: Kinetic Cuirass
    pick_rate: 0.08
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.77
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.44
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.71
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.59
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.31
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.9
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.56
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.53
  - name: Sundering Axe
    pick_rate: 0.16
    win_rate: 0.64
  - name: Warrior's Axe
    pick_rate: 0.15
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-18'
  god_win_rate: 0.5597667638483965
  god_matches_won: 192
  god_matches_played: 343
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-18'
  god_matches_analyzed: 8839
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s Shield,
    Rod of Tahuti, Erosion, Gluttonous Grimoire, Shield of the Phoenix, Eye of Providence,
    Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Spectral Armor, Shield
    Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s Hide,
    Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the Storm,
    Nimble Ring, Magi''s Cloak, Runeforged Hammer, Ancile, Gladiator''s Shield, Shogun''s
    Ofuda, Screeching Gargoyle, Void Shield, Helm of Radiance, Doublet of Binding,
    Hydra''s Lament, Hussar''s Wings, Prophetic Cloak, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.37
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.78
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.62
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.54
      pick: 0.22
      fit: 0.68
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Berserker''s
    Shield, Gluttonous Grimoire, Chandra''s Grace, Rod of Tahuti, Freya''s Tears,
    Rod of Asclepius, Oni Hunter''s Garb, Erosion, Eye of Providence, Phoenix Feather,
    Breastplate of Valor, Draconic Scale, Spectral Armor, Jotunn''s Revenge, Pharaoh''s
    Curse, Leviathan''s Hide, The Crusher, Midgardian Mail, Runeforged Hammer, Eye
    of the Storm, Glorious Pridwen, Lifebinder, Shield Splitter, Nimble Ring, Gladiator''s
    Shield, Ancile, Blood-Bound Book, The Reaper, Shogun''s Ofuda, Void Shield, Doublet
    of Binding, Mantle Of Discord, Stone of Binding, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.34
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.76
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.9
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.22
      fit: 0.66
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Stone of Binding
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
    for this god: Rod of Tahuti, Kinetic Cuirass, Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Stone of Binding, Berserker''s Shield,
    Screeching Gargoyle, Freya''s Tears, Void Shield, Breastplate of Valor, The Cosmic
    Horror, Oni Hunter''s Garb, Void Stone, Spear of the Magus, Shield of the Phoenix,
    Spear of Desolation, Avenging Blade, Erosion, Eye of Providence, Spectral Armor,
    Nimble Ring, Draconic Scale, The Reaper, Obsidian Shard, Pharaoh''s Curse, Riptalon,
    Shield Splitter, Leviathan''s Hide, Runeforged Hammer, Midgardian Mail, Silverbranch
    Bow, Mantle Of Discord, Hydra''s Lament, Eye of the Storm, Helm of Radiance, Ancile.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Berserker''s Shield, Nimble Ring, Rod of Tahuti, Amanita
    Charm, Gluttonous Grimoire, Golden Blade, The Crusher, Pharaoh''s Curse, Freya''s
    Tears, Jotunn''s Revenge, Breastplate of Valor, Riptalon, Oni Hunter''s Garb,
    Soul Gem, Shield of the Phoenix, Shogun''s Ofuda, Tyrfing, Runeforged Hammer,
    Spectral Armor, Erosion, Hydra''s Lament, Lernaean Bow, Silverbranch Bow, Shield
    Splitter, Eye of Providence, Draconic Scale, Eye of the Storm, Leviathan''s Hide,
    Midgardian Mail, Toxic Blade, Mantle Of Discord, Stone of Binding, Helm of Radiance,
    Death Metal, Screeching Gargoyle, Yogi''s Necklace, Damaru, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.2
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.47
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
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
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Freya''s Tears, Breastplate
    of Valor, Jotunn''s Revenge, Shield of the Phoenix, Rod of Tahuti, Amanita Charm,
    Soul Gem, Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The Crusher,
    Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring, Chandra''s
    Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye
    of Providence, Shield Splitter, Draconic Scale, Runeforged Hammer, Prophetic Cloak,
    Pharaoh''s Curse, Eye of the Storm, Leviathan''s Hide, Gem of Focus, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord, Totem of Death, Stone of Binding, Arondight,
    Death Metal, Rod of Asclepius, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Kinetic Cuirass, Rod of Tahuti, The Crusher,
    Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Freya''s
    Tears, Runeforged Hammer, Nimble Ring, Shield Splitter, Breastplate of Valor,
    Hydra''s Lament, Oni Hunter''s Garb, Soul Gem, Golden Blade, Eye of the Storm,
    Shield of the Phoenix, Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence,
    The Reaper, Lernaean Bow, Draconic Scale, Death Metal, Avenging Blade, Damaru,
    The Cosmic Horror, Shogun''s Ofuda, Leviathan''s Hide, Midgardian Mail, Spear
    of the Magus, Mantle Of Discord, Stone of Binding, Tekko-Kagi, Spear of Desolation,
    Helm of Radiance, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.52
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Kinetic Cuirass, Gluttonous
    Grimoire, The Crusher, Jotunn''s Revenge, Amanita Charm, Soul Gem, Berserker''s
    Shield, Nimble Ring, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb,
    The Cosmic Horror, Runeforged Hammer, Shield Splitter, Shield of the Phoenix,
    Death Metal, Spear of the Magus, Hydra''s Lament, Erosion, Spear of Desolation,
    Eye of the Storm, Helm of Radiance, Spectral Armor, Eye of Providence, Draconic
    Scale, Rod of Asclepius, Pharaoh''s Curse, The Reaper, Obsidian Shard, Leviathan''s
    Hide, Golden Blade, Chronos'' Pendant, Jade Scepter, Midgardian Mail, Avenging
    Blade, Mantle Of Discord, Damaru, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.23
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Berserker's Shield
  - Erosion
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s
    Shield, Rod of Tahuti, Erosion, Gluttonous Grimoire, Shield of the Phoenix, Eye
    of Providence, Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Spectral
    Armor, Shield Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the
    Storm, Nimble Ring, Magi''s Cloak, Runeforged Hammer, Ancile, Gladiator''s Shield,
    Shogun''s Ofuda, Screeching Gargoyle, Prophetic Cloak, Void Shield, Helm of Radiance,
    Doublet of Binding, Hydra''s Lament, Hussar''s Wings, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.18
      fit: 0.37
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.13
      fit: 0.78
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
    Erosion:
      total: 0.52
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: *id001
---
