---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.6
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.6
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.18
      win_rate: 0.56
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.43
  - name: Prophetic Cloak
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Transcendence
      pick_rate: 0.17
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.86
    alternates:
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.75
  - name: Blinking Abyss
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 1.0
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 1.0
  - name: Medallion
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 1.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.7
  - name: Selflessness
    pick_rate: 0.2
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-09-09'
  god_win_rate: 0.6530612244897959
  god_matches_won: 32
  god_matches_played: 49
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion, Eye of Providence,
    Draconic Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire,
    Mantle Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban
    Effigy, Void Stone, Spear of Desolation, Spectral Armor, Hussar''s Wings, Rod
    of Asclepius, Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.15
      fit: 0.37
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.78
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.49
    Spirit Robe:
      total: 0.65
      efficiency: 0.34
      win: 1.0
      pick: 0.15
      fit: 0.49
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.62
    Hide of the Nemean Lion:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.28
      fit: 0.44
  community_ordered:
  - Breastplate of Valor
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Soul Gem, Berserker''s Shield, Erosion, Eye of Providence, Draconic
    Scale, Ethereal Staff, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace,
    Shield Splitter, Chandra''s Grace, Runeforged Hammer, Glorious Pridwen, Eye of
    the Storm, Lifebinder, Midgardian Mail, Stone of Binding, Helm of Radiance, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Stampede, Ancile, Oni Hunter''s Garb, Daybreak
    Gavel, Sphere of Negation, Screeching Gargoyle, Void Stone, Mantle Of Discord,
    Spectral Armor, Gladiator''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.15
      fit: 0.34
    Shell of Rebuke:
      total: 0.62
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.41
    Spirit Robe:
      total: 0.68
      efficiency: 0.34
      win: 1.0
      pick: 0.15
      fit: 0.71
    Freya's Tears:
      total: 0.7
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.28
      fit: 0.46
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Breastplate of Valor
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Void Shield, Spear
    of the Magus, Soul Gem, Void Stone, Obsidian Shard, Avenging Blade, Berserker''s
    Shield, Heartseeker, Erosion, Shield Splitter, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Doom Orb, Helm of Radiance, Runeforged Hammer, The World
    Stone, Titan''s Bane, Magi''s Cloak, The Crusher, Dreamer''s Idol, Eye of the
    Storm, Mantle Of Discord, Midgardian Mail, The Reaper, Daybreak Gavel, Rod of
    Asclepius, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.15
      fit: 0.26
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.57
      pick: 0.19
      fit: 0.47
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.34
    Spirit Robe:
      total: 0.63
      efficiency: 0.34
      win: 1.0
      pick: 0.15
      fit: 0.34
    Freya's Tears:
      total: 0.68
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.28
      fit: 0.31
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Nimble Ring, Kinetic
    Cuirass, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield Splitter, Soul Gem,
    Runeforged Hammer, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda,
    Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence, Stone of Binding,
    Eye of the Storm, Shield of the Phoenix, Toxic Blade, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Spear of Desolation, Spear
    of the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod
    of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.3
    Spirit Robe:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.15
      fit: 0.26
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.68
      efficiency: 0.52
      win: 1.0
      pick: 0.28
      fit: 0.24
  community_ordered:
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Shell of Rebuke
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Erosion, Helm of
    Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of
    Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle
    Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace,
    Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.15
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.19
      fit: 0.46
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.32
    Spirit Robe:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.15
      fit: 0.32
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.64
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.28
      fit: 0.29
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Golden Blade, Eye
    of the Storm, Gluttonous Grimoire, Heartseeker, Tyrfing, Lernaean Bow, Erosion,
    Spear of Desolation, Tekko-Kagi, Spear of the Magus, Eye of Providence, Avenging
    Blade, Shield of the Phoenix, Stone of Binding, Draconic Scale, Helm of Radiance,
    Soul Gem, Titan''s Bane, Silverbranch Bow, The Crusher, Obsidian Shard, Pharaoh''s
    Curse, Magi''s Cloak, Toxic Blade, The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching
    Gargoyle, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.15
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.19
      fit: 0.45
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.3
    Spirit Robe:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.15
      fit: 0.3
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.38
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.28
      fit: 0.27
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of Desolation, Spear of the
    Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s
    Shield, Eye of the Storm, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.15
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.19
      fit: 0.41
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.28
      fit: 0.3
    Spirit Robe:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.15
      fit: 0.3
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.38
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.28
      fit: 0.27
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Hide of the Nemean Lion
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion,
    Eye of Providence, Draconic Scale, Berserker''s Shield, Shield Splitter, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm, Helm of Radiance,
    Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Runeforged Hammer, Screeching
    Gargoyle, Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb,
    Helm of Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Spectral Armor,
    Hussar''s Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel, Soul Gem,
    Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.26
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.19
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 0.86
      pick: 0.27
      fit: 0.62
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.6
      pick: 0.2
      fit: 0.68
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
