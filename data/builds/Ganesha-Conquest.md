---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.54
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.38
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.23
      win_rate: 0.47
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.71
  - name: Stampede
    pick_rate: 0.22
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.6
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.42
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.47
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.29
  - name: Genji's Guard
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.19
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.58
    alternates:
    - name: Spirit Robe
      pick_rate: 0.12
      win_rate: 0.75
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.63
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.2
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.6
    - name: Draconic Scale
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.32
    win_rate: 0.33
  - name: Heroism
    pick_rate: 0.24
    win_rate: 0.65
  - name: War Flag
    pick_rate: 0.12
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-11-08'
  god_win_rate: 0.5
  god_matches_won: 65
  god_matches_played: 130
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5134
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Prophetic
    Cloak, Shield of the Phoenix, Gluttonous Grimoire, Breastplate of Valor, Soul
    Gem, Erosion, Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of
    Darkness, Stone of Binding, Midgardian Mail, Screeching Gargoyle, Spear of Desolation,
    Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Hide of
    the Nemean Lion, Lotus Sickle, Gladiator''s Shield, Ancile, Blood-Bound Book,
    Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.76
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.36
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.73
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.45
      win: 0.71
      pick: 0.11
      fit: 0.58
    Draconic Scale:
      total: 0.63
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.63
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Prophetic Cloak
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic
    Cuirass, Rod of Tahuti, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather,
    Yogi''s Necklace, Ethereal Staff, Chandra''s Grace, Breastplate of Valor, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Shifter''s Shield, Midgardian Mail, Bancroft''s
    Talon, Regrowth Striders, Glorious Pridwen, Rod of Asclepius, Spear of Desolation,
    Leviathan''s Hide, Soul Locket, Hide of the Nemean Lion, Gladiator''s Shield,
    Screeching Gargoyle.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.76
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.33
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.45
      win: 0.71
      pick: 0.11
      fit: 0.52
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.86
    Draconic Scale:
      total: 0.63
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.61
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Genji''s Guard, Rod of Tahuti, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of
    Binding, Void Stone, Void Shield, Breastplate of Valor, Obsidian Shard, Shield
    of the Phoenix, Spear of the Magus, Oni Hunter''s Garb, Erosion, Dreamer''s Idol,
    Eye of Providence, Shifter''s Shield, Midgardian Mail, Lotus Sickle, Helm of Radiance,
    Doom Orb, Helm of Darkness, Blood-Bound Book, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.74
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.26
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.6
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.45
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Genji's Guard
  - Bragi's Harp
  - Draconic Scale
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring,
    Oni Hunter''s Garb, Spear of Desolation, Erosion, Lotus Sickle, Eye of Providence,
    Bragi''s Harp, Screeching Gargoyle, Blood-Bound Book, Helm of Radiance, Midgardian
    Mail, Shifter''s Shield, Eros'' Bow, Stone of Binding, Leviathan''s Hide, Magi''s
    Cloak, Mantle Of Discord, Helm of Darkness, Hide of the Nemean Lion, Ancient Signet.'
  slot_scores:
    Nimble Ring:
      total: 0.51
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.3
    Genji's Guard:
      total: 0.74
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.21
    Bragi's Harp:
      total: 0.5
      efficiency: 0.47
      win: 0.59
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.59
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.36
    Eros' Bow:
      total: 0.49
      efficiency: 0.5
      win: 0.59
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
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
  - Prophetic Cloak
  - Draconic Scale
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Prophetic Cloak, Rod
    of Tahuti, Amanita Charm, Soul Gem, Kinetic Cuirass, Breastplate of Valor, Shield
    of the Phoenix, Spear of Desolation, Lotus Sickle, Screeching Gargoyle, Gluttonous
    Grimoire, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s Garb, Erosion,
    Eye of Providence, Helm of Radiance, Blood-Bound Book, Shifter''s Shield, Gem
    of Focus, Heartwood Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace,
    Stone of Binding, Leviathan''s Hide, Regrowth Striders.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.77
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.52
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.45
      win: 0.71
      pick: 0.11
      fit: 0.6
    Draconic Scale:
      total: 0.6
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.42
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Berserker''s
    Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous
    Grimoire, Soul Gem, The Reaper, Tyrfing, Breastplate of Valor, Runeforged Hammer,
    Spear of Desolation, Hydra''s Lament, Shield of the Phoenix, Golden Blade, The
    Crusher, Oni Hunter''s Garb, Heartseeker, Erosion, Death Metal, Eye of Providence,
    Tekko-Kagi, Lotus Sickle, Titan''s Bane, Screeching Gargoyle, Shifter''s Shield,
    Midgardian Mail, Helm of Radiance, Blood-Bound Book, Bragi''s Harp, Obsidian Shard,
    Stone of Binding, Arondight, Avenging Blade, Nimble Ring, Leviathan''s Hide, Helm
    of Darkness, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.74
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.22
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.59
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
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
  - Prophetic Cloak
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Amanita
    Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, Kinetic Cuirass, Spear
    of Desolation, Shield Splitter, Berserker''s Shield, Breastplate of Valor, The
    Reaper, Lotus Sickle, Shield of the Phoenix, Helm of Radiance, Blood-Bound Book,
    Runeforged Hammer, Obsidian Shard, Death Metal, Hydra''s Lament, Oni Hunter''s
    Garb, Helm of Darkness, Spear of the Magus, Ancient Signet, The Crusher, Erosion,
    Eye of Providence, Polynomicon, Chronos'' Pendant, Heartseeker, Dreamer''s Idol,
    Screeching Gargoyle, Shifter''s Shield, Midgardian Mail, Stone of Binding, Jade
    Scepter, Titan''s Bane, Tyrfing, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.74
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.22
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.49
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.45
      win: 0.71
      pick: 0.11
      fit: 0.36
    Draconic Scale:
      total: 0.59
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.39
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s
    Guard, Shield of the Phoenix, Gluttonous Grimoire, Breastplate of Valor, Soul
    Gem, Erosion, Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of
    Darkness, Stone of Binding, Midgardian Mail, Screeching Gargoyle, Spear of Desolation,
    Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Hide of
    the Nemean Lion, Lotus Sickle, Gladiator''s Shield, Prophetic Cloak, Ancile, Blood-Bound
    Book, Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.76
      efficiency: 0.71
      win: 1.0
      pick: 0.13
      fit: 0.36
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.48
      pick: 0.28
      fit: 0.58
    Draconic Scale:
      total: 0.63
      efficiency: 0.53
      win: 0.75
      pick: 0.22
      fit: 0.63
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
---
