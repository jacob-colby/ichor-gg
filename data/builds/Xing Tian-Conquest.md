---
type: smite-build
god: Xing Tian
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relentless Spite
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.38
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.33
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.66
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.46
  - name: Stampede
    pick_rate: 0.16
    win_rate: 0.7
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.38
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.44
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.64
  - name: Sundering Echo
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.83
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.39
    win_rate: 0.51
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.72
  - name: Heroism
    pick_rate: 0.08
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/xing-tian/
  last_verified: '2026-11-06'
  god_win_rate: 0.5586206896551724
  god_matches_won: 81
  god_matches_played: 145
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Draconic Scale, Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Gluttonous
    Grimoire, Shield of the Phoenix, Soul Gem, Erosion, Breastplate of Valor, Eye
    of Providence, Oni Hunter''s Garb, Helm of Darkness, Stone of Binding, Midgardian
    Mail, Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle, Leviathan''s Hide,
    Spear of Desolation, Helm of Radiance, Gladiator''s Shield, Blood-Bound Book,
    Ancile, Prophetic Cloak, Void Stone.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.34
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.28
      fit: 0.57
    Draconic Scale:
      total: 0.66
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.63
    Shifter's Shield:
      total: 0.58
      efficiency: 0.5
      win: 0.66
      pick: 0.2
      fit: 0.63
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Draconic Scale
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Draconic Scale, Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic
    Cuirass, Rod of Tahuti, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather,
    Yogi''s Necklace, Ethereal Staff, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Chandra''s Grace, Breastplate of Valor, Bancroft''s Talon, Midgardian Mail, Regrowth
    Striders, Glorious Pridwen, Leviathan''s Hide, Spear of Desolation, Gladiator''s
    Shield, Screeching Gargoyle, Helm of Darkness.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.31
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.85
    Draconic Scale:
      total: 0.66
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.61
    Shifter's Shield:
      total: 0.57
      efficiency: 0.5
      win: 0.66
      pick: 0.2
      fit: 0.61
    Amanita Charm:
      total: 0.65
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Draconic Scale, Rod of Tahuti, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Kinetic Cuirass, Screeching Gargoyle, Stone of Binding, Spear of Desolation,
    Void Stone, Void Shield, Obsidian Shard, Breastplate of Valor, Shield of the Phoenix,
    Spear of the Magus, Oni Hunter''s Garb, Erosion, Dreamer''s Idol, Eye of Providence,
    Midgardian Mail, Helm of Radiance, Doom Orb, Blood-Bound Book, Helm of Darkness,
    Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.25
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.28
      fit: 0.41
    Draconic Scale:
      total: 0.63
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring,
    Oni Hunter''s Garb, Erosion, Spear of Desolation, Eye of Providence, Bragi''s
    Harp, Blood-Bound Book, Helm of Radiance, Screeching Gargoyle, Midgardian Mail,
    Stone of Binding, Leviathan''s Hide, Magi''s Cloak, Helm of Darkness, Mantle Of
    Discord, Ancient Signet, Death Metal.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.2
    Nimble Ring:
      total: 0.51
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.5
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.62
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Amanita
    Charm, Soul Gem, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Screeching Gargoyle, Gluttonous Grimoire, Chronos'' Pendant,
    Gladiator''s Shield, Oni Hunter''s Garb, Prophetic Cloak, Erosion, Eye of Providence,
    Blood-Bound Book, Helm of Radiance, Gem of Focus, Heartwood Charm, Helm of Darkness,
    Midgardian Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide, Regrowth
    Striders.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.44
    Genji's Guard:
      total: 0.63
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.6
      pick: 0.28
      fit: 0.59
    Draconic Scale:
      total: 0.63
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.41
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Berserker''s
    Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous
    Grimoire, Soul Gem, The Reaper, Tyrfing, Runeforged Hammer, Breastplate of Valor,
    Spear of Desolation, Hydra''s Lament, Golden Blade, Shield of the Phoenix, The
    Crusher, Oni Hunter''s Garb, Heartseeker, Erosion, Death Metal, Eye of Providence,
    Tekko-Kagi, Titan''s Bane, Blood-Bound Book, Screeching Gargoyle, Midgardian Mail,
    Helm of Radiance, Bragi''s Harp, Obsidian Shard, Stone of Binding, Nimble Ring,
    Avenging Blade, Leviathan''s Hide, Arondight, Helm of Darkness, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.21
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.62
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Amanita
    Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Jotunn''s Revenge, Shield
    Splitter, Spear of Desolation, Berserker''s Shield, The Reaper, Breastplate of
    Valor, Blood-Bound Book, Helm of Radiance, Runeforged Hammer, Shield of the Phoenix,
    Obsidian Shard, Death Metal, Oni Hunter''s Garb, Helm of Darkness, Hydra''s Lament,
    Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye of Providence, Polynomicon,
    Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Screeching Gargoyle, Midgardian
    Mail, Stone of Binding, Jade Scepter, Tyrfing, Titan''s Bane, Leviathan''s Hide,
    Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.38
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.21
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.28
      fit: 0.35
    Draconic Scale:
      total: 0.62
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Draconic Scale
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Gluttonous
    Grimoire, Draconic Scale, Shield of the Phoenix, Soul Gem, Erosion, Breastplate
    of Valor, Eye of Providence, Oni Hunter''s Garb, Helm of Darkness, Stone of Binding,
    Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle, Leviathan''s
    Hide, Spear of Desolation, Helm of Radiance, Gladiator''s Shield, Blood-Bound
    Book, Ancile, Prophetic Cloak, Void Stone.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.68
      pick: 0.25
      fit: 0.34
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.28
      fit: 0.57
    Draconic Scale:
      total: 0.66
      efficiency: 0.53
      win: 0.83
      pick: 0.11
      fit: 0.63
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
---
