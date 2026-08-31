---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.48
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.29
    win_rate: 0.61
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.24
      win_rate: 0.32
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.68
  - name: Breastplate of Valor
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.39
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.54
  - name: Genji's Guard
    pick_rate: 0.28
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.37
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.71
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.57
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.53
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.54
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.36
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.63
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.57
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.31
    win_rate: 0.44
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.58
  - name: War Banner
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-31'
  god_win_rate: 0.5173913043478261
  god_matches_won: 119
  god_matches_played: 230
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-31'
  god_matches_analyzed: 7103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Stampede, Kinetic Cuirass,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Hydra''s Lament, Magi''s Cloak, Helm
    of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Leviathan''s Hide, Void Shield, Ancile, Heartseeker,
    Oni Hunter''s Garb, Spear of Desolation, Prophetic Cloak, Daybreak Gavel, Rod
    of Asclepius, Void Stone, Xibalban Effigy, Spectral Armor, Helm of Darkness, Soul
    Gem, Spear of the Magus, Draconic Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.25
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.37
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.52
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.29
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.57
    Stampede:
      total: 0.54
      efficiency: 0.51
      win: 0.68
      pick: 0.08
      fit: 0.37
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
  - Shield of the Phoenix
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Stampede, Kinetic Cuirass, Rod of Asclepius, Shield Splitter, Soul Gem, Eye of
    the Storm, Berserker''s Shield, Erosion, Ethereal Staff, Eye of Providence, The
    Reaper, Yogi''s Necklace, Hydra''s Lament, Phoenix Feather, Gluttonous Grimoire,
    Avenging Blade, Chandra''s Grace, Glorious Pridwen, Lifebinder, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Daybreak Gavel, Magi''s Cloak, Leviathan''s
    Hide, Void Shield, Sphere of Negation, Ancile, Screeching Gargoyle, Heartseeker,
    Oni Hunter''s Garb, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.39
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.46
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.29
      fit: 0.56
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.86
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.68
      pick: 0.08
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: anti-tank
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
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Kinetic Cuirass, Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle, Void
    Shield, Spear of Desolation, Heartseeker, Spear of the Magus, Shield Splitter,
    Void Stone, Soul Gem, Obsidian Shard, Berserker''s Shield, Titan''s Bane, The
    Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s Lament, Eye of Providence,
    Shield of the Phoenix, Helm of Radiance, Doom Orb, The World Stone, Magi''s Cloak,
    Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Mantle Of Discord, Midgardian
    Mail, Daybreak Gavel, Rod of Asclepius, Draconic Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.38
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.29
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.42
    Stampede:
      total: 0.53
      efficiency: 0.51
      win: 0.68
      pick: 0.08
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Nimble Ring
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield
    Splitter, Pharaoh''s Curse, Soul Gem, Riptalon, Lernaean Bow, Shogun''s Ofuda,
    Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence, Stone of Binding,
    Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic Blade, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Midgardian Mail, Mantle
    Of Discord, Spear of Desolation, Bragi''s Harp, Spear of the Magus, Tekko-Kagi,
    Rod of Asclepius, Avenging Blade, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.25
      fit: 0.2
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.33
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.29
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
  - Shifter's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Hydra''s
    Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter, Berserker''s
    Shield, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of
    Providence, Gladiator''s Shield, Stone of Binding, Eye of the Storm, Arondight,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s
    Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield, Draconic
    Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.51
      pick: 0.44
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.25
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.29
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.54
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
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Eye of
    the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Lernaean Bow, Erosion,
    Spear of Desolation, Tekko-Kagi, Eye of Providence, Tyrfing, Avenging Blade, Spear
    of the Magus, Shield of the Phoenix, Stone of Binding, Helm of Radiance, Titan''s
    Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak,
    The Reaper, Silverbranch Bow, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.38
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.29
      fit: 0.42
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Spear of the Magus, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s
    Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail, Draconic
    Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.38
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.29
      fit: 0.42
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.42
    Stampede:
      total: 0.53
      efficiency: 0.51
      win: 0.68
      pick: 0.08
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
      win: 0.54
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.18
      fit: 0.52
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.29
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.57
  starter: *id001
---
