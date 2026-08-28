---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.44
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.48
    - name: Golden Blade
      pick_rate: 0.11
      win_rate: 0.35
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.55
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.54
  - name: Stampede
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.29
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.47
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.73
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.63
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.67
  - name: Shield
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.6
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.5
  - name: Selflessness
    pick_rate: 0.15
    win_rate: 0.52
  - name: Warrior's Axe
    pick_rate: 0.12
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-28'
  god_win_rate: 0.5031847133757962
  god_matches_won: 79
  god_matches_played: 157
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-28'
  god_matches_analyzed: 3498
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Stampede
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Hide
    of the Nemean Lion, Stampede, Jotunn''s Revenge, Breastplate of Valor, Erosion,
    Eye of Providence, Draconic Scale, Berserker''s Shield, Shield Splitter, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm, Helm of Radiance,
    Mantle Of Discord, Gluttonous Grimoire, Runeforged Hammer, Midgardian Mail, Screeching
    Gargoyle, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of
    Darkness, Xibalban Effigy, Void Stone, Spectral Armor, Spear of Desolation, Hussar''s
    Wings, Gladiator''s Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding,
    Hydra''s Lament, Soul Gem, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.78
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.11
      fit: 0.44
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.68
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.44
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Hide of the Nemean Lion
  - Stampede
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Hide of the Nemean Lion, Rod of Asclepius, Stampede, Jotunn''s
    Revenge, Soul Gem, Breastplate of Valor, Berserker''s Shield, Erosion, Eye of
    Providence, Draconic Scale, Ethereal Staff, Phoenix Feather, Gluttonous Grimoire,
    Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Runeforged Hammer, Eye of
    the Storm, Glorious Pridwen, Midgardian Mail, Stone of Binding, Lifebinder, Helm
    of Radiance, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s
    Garb, Daybreak Gavel, Screeching Gargoyle, Sphere of Negation, Void Stone, Mantle
    Of Discord, Spectral Armor, Gladiator''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.9
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.11
      fit: 0.46
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.54
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.96
    Stampede:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s Revenge, Amanita Charm,
    Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear
    of Desolation, Hide of the Nemean Lion, Void Shield, Spear of the Magus, Breastplate
    of Valor, Soul Gem, Void Stone, Obsidian Shard, Avenging Blade, Berserker''s Shield,
    Heartseeker, Erosion, Shield Splitter, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Doom Orb, Helm of Radiance, Runeforged Hammer, The World Stone,
    Titan''s Bane, Magi''s Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm,
    Mantle Of Discord, Midgardian Mail, The Reaper, Daybreak Gavel, Rod of Asclepius,
    Leviathan''s Hide, Hydra''s Lament.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.43
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Freya''s Tears, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Nimble Ring, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor,
    Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye
    of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s
    Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak
    Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian
    Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade, Golden
    Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.53
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Spear of Desolation, Hide of the Nemean Lion, Hydra''s Lament, Screeching Gargoyle,
    Soul Gem, Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Erosion, Helm
    of Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of
    Focus, Prophetic Cloak, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear
    of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Chandra''s Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.64
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Freya''s
    Tears, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Breastplate of Valor, Eye of the Storm, Gluttonous Grimoire, Hydra''s
    Lament, Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Eye of Providence, Spear of the Magus, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Helm of Radiance, Titan''s Bane, Soul Gem, The
    Crusher, Obsidian Shard, Pharaoh''s Curse, Silverbranch Bow, Magi''s Cloak, The
    Reaper, Nimble Ring, Toxic Blade, Shogun''s Ofuda, Screeching Gargoyle, Mantle
    Of Discord, Midgardian Mail, Golden Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Hide of the Nemean Lion
  - Stampede
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter,
    Breastplate of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer,
    Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of the Storm,
    Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield
    of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.11
      fit: 0.27
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.42
    Stampede:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.12
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Mantle Of Discord, Gluttonous
    Grimoire, Runeforged Hammer, Midgardian Mail, Screeching Gargoyle, Hide of the
    Nemean Lion, Prophetic Cloak, Leviathan''s Hide, Void Shield, Stampede, Ancile,
    Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spectral Armor,
    Spear of Desolation, Hussar''s Wings, Gladiator''s Shield, Rod of Asclepius, Daybreak
    Gavel, Doublet of Binding, Hydra''s Lament, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.46
      pick: 0.2
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.11
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.18
      fit: 0.68
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.68
  starter: *id001
---
