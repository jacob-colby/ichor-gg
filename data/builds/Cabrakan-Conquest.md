---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.4
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.51
    win_rate: 0.67
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 1.0
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.67
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.75
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.6
    - name: Contagion
      pick_rate: 0.1
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.8
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.14
      win_rate: 0.6
    - name: Sundering Echo
      pick_rate: 0.11
      win_rate: 0.75
  - name: Contagion
    pick_rate: 0.15
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.75
    - name: Hide of the Nemean Lion
      pick_rate: 0.12
      win_rate: 0.5
  - name: Sundering Echo
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Sage's Ring
      pick_rate: 0.1
      win_rate: 1.0
    - name: Regrowth Striders
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.46
    win_rate: 0.79
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.2
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-10-22'
  god_win_rate: 0.6097560975609756
  god_matches_won: 25
  god_matches_played: 41
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Runeforged Hammer
  - Contagion
  - Jotunn's Revenge
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield Splitter, Breastplate
    of Valor, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Hydra''s Lament, Magi''s Cloak,
    Helm of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Leviathan''s Hide, Void Shield, Ancile, Heartseeker,
    Oni Hunter''s Garb, Spear of Desolation, Prophetic Cloak, Daybreak Gavel, Rod
    of Asclepius, Void Stone, Xibalban Effigy, Spectral Armor, Stampede, Helm of Darkness,
    Soul Gem, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.31
    Runeforged Hammer:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.51
      fit: 0.48
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.32
      fit: 0.26
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.37
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.23
      fit: 0.57
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  - Contagion
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Contagion
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Rod of Asclepius, Shield Splitter, Soul Gem, Eye of the Storm, Breastplate of
    Valor, Berserker''s Shield, Erosion, Ethereal Staff, Eye of Providence, The Reaper,
    Draconic Scale, Yogi''s Necklace, Hydra''s Lament, Phoenix Feather, Gluttonous
    Grimoire, Avenging Blade, Chandra''s Grace, Glorious Pridwen, Lifebinder, Stone
    of Binding, Midgardian Mail, Helm of Radiance, Daybreak Gavel, Magi''s Cloak,
    Leviathan''s Hide, Void Shield, Sphere of Negation, Ancile, Screeching Gargoyle,
    Heartseeker, Oni Hunter''s Garb, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.28
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.32
      fit: 0.31
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.39
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.53
      win: 0.69
      pick: 0.0
      fit: 0.8
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.23
      fit: 0.56
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Genji's Guard
  - Contagion
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Contagion
  - Genji's Guard
  - Jotunn's Revenge
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle, Void Shield, Spear of
    Desolation, Breastplate of Valor, Heartseeker, Spear of the Magus, Shield Splitter,
    Void Stone, Soul Gem, Obsidian Shard, Berserker''s Shield, Titan''s Bane, The
    Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s Lament, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Helm of Radiance, Doom Orb, The World Stone,
    Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.7
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.32
      fit: 0.22
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.23
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.23
      fit: 0.42
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Contagion
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Contagion
  - Genji's Guard
  - Berserker's Shield
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Golden Blade, Gluttonous Grimoire, Breastplate of Valor, Tyrfing,
    Shield Splitter, Pharaoh''s Curse, Soul Gem, Riptalon, Lernaean Bow, Shogun''s
    Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence, Stone of
    Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic Blade,
    Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper,
    Midgardian Mail, Mantle Of Discord, Spear of Desolation, Bragi''s Harp, Spear
    of the Magus, Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.69
      pick: 0.0
      fit: 0.54
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.32
      fit: 0.2
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.2
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.69
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Contagion
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Contagion
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear of Desolation,
    Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter,
    Berserker''s Shield, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire,
    Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye
    of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of
    Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail,
    Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter,
    Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.48
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.32
      fit: 0.23
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.23
      fit: 0.45
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Contagion
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Contagion
  - Runeforged Hammer
  - Berserker's Shield
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Shield Splitter, Breastplate of Valor, Golden Blade, Eye
    of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Lernaean Bow,
    Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence, Tyrfing, Avenging
    Blade, Spear of the Magus, Shield of the Phoenix, Stone of Binding, Draconic Scale,
    Helm of Radiance, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s
    Curse, Magi''s Cloak, The Reaper, Silverbranch Bow, Nimble Ring, Shogun''s Ofuda,
    Screeching Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.23
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.32
      fit: 0.22
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.51
      fit: 0.44
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.69
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Contagion
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Runeforged Hammer
  - Contagion
  - Jotunn's Revenge
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Shield Splitter, Breastplate of Valor, Spear
    of Desolation, Spear of the Magus, Helm of Radiance, Soul Gem, Obsidian Shard,
    Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade,
    Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm of Darkness, Titan''s
    Bane, The Crusher, Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s
    Idol, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.23
      fit: 0.23
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.51
      fit: 0.4
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.32
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.23
      fit: 0.42
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Runeforged Hammer
  - Contagion
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield
    Splitter, Breastplate of Valor, Eye of the Storm, Berserker''s Shield, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Hydra''s
    Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Void
    Shield, Stampede, Ancile, Heartseeker, Oni Hunter''s Garb, Spear of Desolation,
    Prophetic Cloak, Daybreak Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy,
    Spectral Armor, Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.23
      fit: 0.67
    Shield Splitter:
      total: 0.6
      efficiency: 0.55
      win: 0.69
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.28
      fit: 0.52
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.23
      fit: 0.57
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
