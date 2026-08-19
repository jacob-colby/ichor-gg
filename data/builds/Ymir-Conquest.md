---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.6
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.52
    - name: Resolute Mantle
      pick_rate: 0.11
      win_rate: 0.62
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.63
    - name: Spirit Robe
      pick_rate: 0.09
      win_rate: 0.51
  - name: Stampede
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.59
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.66
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.7
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.61
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.69
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.55
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.64
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.63
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.18
    win_rate: 0.66
  - name: Sundering Axe
    pick_rate: 0.12
    win_rate: 0.67
  - name: Selflessness
    pick_rate: 0.11
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-19'
  god_win_rate: 0.5571776155717761
  god_matches_won: 229
  god_matches_played: 411
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
    this god: Kinetic Cuirass, Freya''s Tears, Amanita Charm, Draconic Scale, Erosion,
    Shield of the Phoenix, Eye of Providence, Hide of the Nemean Lion, Oni Hunter''s
    Garb, Rod of Tahuti, Breastplate of Valor, Gluttonous Grimoire, Spectral Armor,
    Nimble Ring, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding,
    Magi''s Cloak, Ancile, Gladiator''s Shield, Soul Gem, Helm of Radiance, Prophetic
    Cloak, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.6
      pick: 0.18
      fit: 0.72
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.65
      pick: 0.13
      fit: 0.72
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.72
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Draconic Scale, Soul Gem, Chandra''s Grace, Rod of Asclepius, Gluttonous Grimoire,
    Hide of the Nemean Lion, Oni Hunter''s Garb, Erosion, Eye of Providence, Rod of
    Tahuti, Phoenix Feather, Spectral Armor, Breastplate of Valor, Leviathan''s Hide,
    Nimble Ring, Midgardian Mail, Lifebinder, Glorious Pridwen, Gladiator''s Shield,
    Ancile, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.2
      fit: 0.35
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.57
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.65
      pick: 0.13
      fit: 0.7
    Amanita Charm:
      total: 0.65
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Stone of Binding, Screeching Gargoyle, Draconic Scale,
    Void Shield, The Cosmic Horror, Breastplate of Valor, Oni Hunter''s Garb, Spear
    of the Magus, Void Stone, Shield of the Phoenix, Spear of Desolation, Nimble Ring,
    Erosion, Eye of Providence, Spectral Armor, Obsidian Shard, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.2
      fit: 0.25
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.61
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Freya''s Tears, Kinetic Cuirass, Amanita Charm, Rod of
    Tahuti, Gluttonous Grimoire, Breastplate of Valor, Draconic Scale, Oni Hunter''s
    Garb, Shield of the Phoenix, Soul Gem, Spectral Armor, Erosion, Eye of Providence,
    Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Helm of Radiance, Stone
    of Binding, Death Metal, Screeching Gargoyle, Bracer of The Abyss, Ancile, Yogi''s
    Necklace, Rod of Asclepius.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.48
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.42
      win: 0.61
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Shield of the Phoenix
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Rod of Tahuti, Soul Gem,
    Gluttonous Grimoire, Draconic Scale, Nimble Ring, Screeching Gargoyle, Oni Hunter''s
    Garb, Chronos'' Pendant, Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral
    Armor, Eye of Providence, Spear of Desolation, Prophetic Cloak, Leviathan''s Hide,
    Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.64
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.65
      pick: 0.13
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Gluttonous Grimoire
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Jotunn''s Revenge,
    Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield, Amanita
    Charm, Nimble Ring, Runeforged Hammer, Draconic Scale, Shield Splitter, Breastplate
    of Valor, Hydra''s Lament, Soul Gem, Oni Hunter''s Garb, Golden Blade, Eye of
    the Storm, Shield of the Phoenix, Pharaoh''s Curse, Erosion, Spectral Armor, Eye
    of Providence, The Reaper, Lernaean Bow, Death Metal, Avenging Blade, The Cosmic
    Horror, Damaru, Shogun''s Ofuda, Leviathan''s Hide, Spear of the Magus, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Helm of Radiance, Spear of Desolation,
    Tekko-Kagi, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Freya''s Tears, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Soul Gem, Nimble Ring, Draconic Scale, Breastplate of Valor,
    Oni Hunter''s Garb, The Cosmic Horror, Runeforged Hammer, Death Metal, Shield
    Splitter, Shield of the Phoenix, Spear of the Magus, Hydra''s Lament, Erosion,
    Helm of Radiance, Spectral Armor, Spear of Desolation, Eye of the Storm, Eye of
    Providence, Pharaoh''s Curse, Rod of Asclepius, Golden Blade, The Reaper, Leviathan''s
    Hide, Obsidian Shard, Jade Scepter, Chronos'' Pendant, Midgardian Mail, Avenging
    Blade, Damaru, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Erosion,
    Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb, Draconic Scale,
    Rod of Tahuti, Breastplate of Valor, Gluttonous Grimoire, Spectral Armor, Nimble
    Ring, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding,
    Magi''s Cloak, Ancile, Gladiator''s Shield, Soul Gem, Helm of Radiance, Prophetic
    Cloak, Hide of the Nemean Lion, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.66
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.6
      pick: 0.18
      fit: 0.72
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.72
  starter: *id001
---
