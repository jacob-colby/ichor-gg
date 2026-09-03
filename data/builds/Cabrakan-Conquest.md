---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.48
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.26
      win_rate: 0.44
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.65
  - name: Breastplate of Valor
    pick_rate: 0.18
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.45
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.69
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.68
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.47
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.59
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.55
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.6
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.3
    win_rate: 0.44
  - name: Bumba's Hammer
    pick_rate: 0.23
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.08
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-09-03'
  god_win_rate: 0.5083798882681564
  god_matches_won: 182
  god_matches_played: 358
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-03'
  god_matches_analyzed: 10626
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield Splitter, Stampede,
    Kinetic Cuirass, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Stone of Binding, Hydra''s Lament, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Void Shield, Ancile,
    Heartseeker, Oni Hunter''s Garb, Spear of Desolation, Prophetic Cloak, Daybreak
    Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy, Spectral Armor, Helm of
    Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.25
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.37
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.52
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shifter's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Stampede, Rod of Asclepius, Shield Splitter, Soul Gem, Eye of the Storm, Berserker''s
    Shield, Kinetic Cuirass, Erosion, Ethereal Staff, Eye of Providence, The Reaper,
    Draconic Scale, Yogi''s Necklace, Hydra''s Lament, Phoenix Feather, Gluttonous
    Grimoire, Avenging Blade, Chandra''s Grace, Glorious Pridwen, Lifebinder, Stone
    of Binding, Midgardian Mail, Helm of Radiance, Daybreak Gavel, Magi''s Cloak,
    Leviathan''s Hide, Void Shield, Sphere of Negation, Ancile, Screeching Gargoyle,
    Heartseeker, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.39
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.46
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.56
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.86
    Stampede:
      total: 0.53
      efficiency: 0.51
      win: 0.65
      pick: 0.06
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle, Void Shield, Spear of
    Desolation, Heartseeker, Spear of the Magus, Shield Splitter, Void Stone, Soul
    Gem, Obsidian Shard, Berserker''s Shield, Titan''s Bane, The Crusher, Kinetic
    Cuirass, Eye of the Storm, Erosion, The Reaper, Hydra''s Lament, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Helm of Radiance, Doom Orb, The World Stone,
    Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.7
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.38
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Nimble Ring, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield Splitter, Pharaoh''s
    Curse, Soul Gem, Riptalon, Lernaean Bow, Shogun''s Ofuda, Kinetic Cuirass, Silverbranch
    Bow, Erosion, Helm of Radiance, Eye of Providence, Stone of Binding, Eye of the
    Storm, Shield of the Phoenix, Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Midgardian Mail, Mantle
    Of Discord, Spear of Desolation, Bragi''s Harp, Spear of the Magus, Tekko-Kagi,
    Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Shield of the Phoenix, Spear of Desolation, Hydra''s Lament, Screeching
    Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Prophetic
    Cloak, Kinetic Cuirass, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of
    Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye of the
    Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus,
    Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak
    Gavel, Chandra''s Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.25
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Shield Splitter, Golden Blade, Eye of the Storm, Gluttonous
    Grimoire, Hydra''s Lament, Heartseeker, Kinetic Cuirass, Lernaean Bow, Erosion,
    Spear of Desolation, Tekko-Kagi, Eye of Providence, Tyrfing, Avenging Blade, Spear
    of the Magus, Shield of the Phoenix, Stone of Binding, Draconic Scale, Helm of
    Radiance, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s Curse,
    Magi''s Cloak, The Reaper, Silverbranch Bow, Nimble Ring, Shogun''s Ofuda, Screeching
    Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.38
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Shield Splitter, Spear of Desolation, Spear
    of the Magus, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield,
    Eye of the Storm, Kinetic Cuirass, Hydra''s Lament, Rod of Asclepius, Heartseeker,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade,
    Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm of Darkness, Titan''s
    Bane, The Crusher, Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s
    Idol, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.38
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
    Stampede:
      total: 0.51
      efficiency: 0.51
      win: 0.65
      pick: 0.06
      fit: 0.27
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Hydra''s
    Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Void
    Shield, Stampede, Ancile, Heartseeker, Oni Hunter''s Garb, Spear of Desolation,
    Prophetic Cloak, Daybreak Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy,
    Spectral Armor, Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.13
      fit: 0.67
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.52
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.57
  starter: *id001
---
