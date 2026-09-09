---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.18
  aspect_win_rate: 0.67
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.21
    win_rate: 0.43
    alternates:
    - name: Stampede
      pick_rate: 0.21
      win_rate: 0.86
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.43
    alternates:
    - name: Stampede
      pick_rate: 0.18
      win_rate: 0.83
    - name: Stygian Anchor
      pick_rate: 0.09
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 1.0
    - name: Stone of Binding
      pick_rate: 0.07
      win_rate: 1.0
  - name: Spirit Robe
    pick_rate: 0.17
    win_rate: 0.75
    alternates:
    - name: Midgardian Mail
      pick_rate: 0.08
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.0
  - name: Veve Charm
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 1.0
    - name: Engraved Guard
      pick_rate: 0.1
      win_rate: 0.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.6
  - name: Warrior's Axe
    pick_rate: 0.18
    win_rate: 0.33
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-09-09'
  god_win_rate: 0.6363636363636364
  god_matches_won: 21
  god_matches_played: 33
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
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Stampede
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Stampede
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Stone of Binding, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Magi''s Cloak,
    Eye of the Storm, Helm of Radiance, Mantle Of Discord, Gluttonous Grimoire, Runeforged
    Hammer, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic Cloak, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spectral Armor, Spear of Desolation, Hussar''s Wings, Gladiator''s
    Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding, Hydra''s Lament,
    Soul Gem.'
  slot_scores:
    Stone of Binding:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.12
      fit: 0.59
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.2
      fit: 0.62
    Stampede:
      total: 0.63
      efficiency: 0.51
      win: 0.83
      pick: 0.25
      fit: 0.44
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Stone of Binding
  - Freya's Tears
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Stampede
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Stone of Binding, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Shifter''s Shield, Rod of Asclepius, Jotunn''s Revenge, Soul
    Gem, Breastplate of Valor, Berserker''s Shield, Erosion, Eye of Providence, Draconic
    Scale, Ethereal Staff, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace,
    Shield Splitter, Chandra''s Grace, Runeforged Hammer, Eye of the Storm, Glorious
    Pridwen, Lifebinder, Hide of the Nemean Lion, Helm of Radiance, Leviathan''s Hide,
    Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Screeching
    Gargoyle, Sphere of Negation, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.12
      fit: 0.51
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.66
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.9
    Stampede:
      total: 0.63
      efficiency: 0.51
      win: 0.83
      pick: 0.25
      fit: 0.46
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.75
      pick: 0.2
      fit: 0.54
    Amanita Charm:
      total: 0.71
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Stone of Binding
  - Stampede
  - Freya's Tears
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
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Stone of Binding, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Spear of the Magus, Breastplate of Valor, Soul Gem, Void Stone, Shifter''s
    Shield, Obsidian Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion,
    Shield Splitter, Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s
    Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, The
    Reaper, Daybreak Gavel, Hide of the Nemean Lion, Rod of Asclepius, Leviathan''s
    Hide, Hydra''s Lament.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.61
      efficiency: 0.51
      win: 0.75
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.75
      efficiency: 0.51
      win: 1.0
      pick: 0.12
      fit: 0.74
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.2
      fit: 0.43
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Stone of Binding
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Stone of Binding, Rod of Tahuti, Berserker''s Shield, Amanita Charm,
    Jotunn''s Revenge, Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire,
    Breastplate of Valor, Tyrfing, Shifter''s Shield, Shield Splitter, Runeforged
    Hammer, Soul Gem, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch
    Bow, Erosion, Helm of Radiance, Eye of Providence, Eye of the Storm, Shield of
    the Phoenix, Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus,
    Bragi''s Harp, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.52
      win: 0.75
      pick: 0.0
      fit: 0.54
    Stone of Binding:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.12
      fit: 0.36
    Berserker's Shield:
      total: 0.64
      efficiency: 0.68
      win: 0.75
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Stone of Binding
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Stone of Binding
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Stone of Binding, Rod of Tahuti, Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Shifter''s
    Shield, Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak,
    Erosion, Helm of Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Eye of the Storm, Arondight, Gem of Focus,
    Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of
    Discord, Glorious Pridwen, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Hide
    of the Nemean Lion, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.12
      fit: 0.42
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.75
      pick: 0.2
      fit: 0.64
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Stone of Binding
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Stone of Binding, Rod of Tahuti, Jotunn''s
    Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Runeforged Hammer, Breastplate of Valor, Golden Blade, Shifter''s Shield, Eye
    of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Tyrfing, Lernaean
    Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence, Spear of the
    Magus, Avenging Blade, Shield of the Phoenix, Draconic Scale, Helm of Radiance,
    Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s Curse, Silverbranch
    Bow, Magi''s Cloak, The Reaper, Nimble Ring, Toxic Blade, Shogun''s Ofuda, Screeching
    Gargoyle, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.12
      fit: 0.4
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.75
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.2
      fit: 0.38
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Stone of Binding
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Stampede
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Stone of Binding, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter,
    Breastplate of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer,
    Helm of Radiance, Soul Gem, Shifter''s Shield, Obsidian Shard, Berserker''s Shield,
    Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion, Eye
    of Providence, Shield of the Phoenix, Draconic Scale, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol.'
  slot_scores:
    Stone of Binding:
      total: 0.69
      efficiency: 0.51
      win: 1.0
      pick: 0.12
      fit: 0.4
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.52
    Stampede:
      total: 0.6
      efficiency: 0.51
      win: 0.83
      pick: 0.25
      fit: 0.27
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.2
      fit: 0.38
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Stone of Binding
  - Stampede
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Mantle Of Discord, Gluttonous
    Grimoire, Runeforged Hammer, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic
    Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness,
    Xibalban Effigy, Void Stone, Spectral Armor, Spear of Desolation, Hussar''s Wings,
    Gladiator''s Shield, Rod of Asclepius, Daybreak Gavel, Doublet of Binding, Hydra''s
    Lament, Soul Gem.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.75
      pick: 0.0
      fit: 0.25
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.43
      pick: 0.29
      fit: 0.37
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.2
      fit: 0.62
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
