---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.34
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.32
    win_rate: 0.43
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.58
    - name: Chronos' Pendant
      pick_rate: 0.09
      win_rate: 0.45
  - name: Stampede
    pick_rate: 0.19
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.38
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.45
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.44
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.56
  - name: Spirit Robe
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.75
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.38
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.2
    alternates:
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.8
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.75
  - name: Legionnaire Armor
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Engraved Guard
      pick_rate: 0.14
      win_rate: 0.67
    - name: Stygian Anchor
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.35
    win_rate: 0.34
  - name: Heroism
    pick_rate: 0.15
    win_rate: 0.76
  - name: Conduit Gem
    pick_rate: 0.1
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-08-14'
  god_win_rate: 0.41025641025641024
  god_matches_won: 48
  god_matches_played: 117
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Breastplate of Valor, Kinetic Cuirass, Amanita Charm,
    Rod of Tahuti, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Shifter''s
    Shield, Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Spectral Armor,
    Soul Gem, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding,
    Nimble Ring, Gladiator''s Shield, Magi''s Cloak, Screeching Gargoyle, Ancile,
    Prophetic Cloak, Helm of Radiance, Hide of the Nemean Lion.'
  slot_scores:
    Stygian Anchor:
      total: 0.68
      efficiency: 0.41
      win: 1.0
      pick: 0.15
      fit: 0.5
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.45
      pick: 0.3
      fit: 0.4
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.65
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.7
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Stygian Anchor
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Breastplate of
    Valor, Kinetic Cuirass, Soul Gem, Gluttonous Grimoire, Chandra''s Grace, Rod of
    Tahuti, Rod of Asclepius, Oni Hunter''s Garb, Erosion, Shifter''s Shield, Eye
    of Providence, Draconic Scale, Phoenix Feather, Spectral Armor, Leviathan''s Hide,
    Midgardian Mail, Glorious Pridwen, Lifebinder, Gladiator''s Shield, Nimble Ring,
    Blood-Bound Book, Ancile, Hide of the Nemean Lion.'
  slot_scores:
    Stygian Anchor:
      total: 0.66
      efficiency: 0.41
      win: 1.0
      pick: 0.15
      fit: 0.42
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Rod of Tahuti, Breastplate of Valor, Gluttonous
    Grimoire, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding, Screeching
    Gargoyle, Void Shield, The Cosmic Horror, Spear of the Magus, Oni Hunter''s Garb,
    Shield of the Phoenix, Spear of Desolation, Void Stone, Erosion, Shifter''s Shield,
    Eye of Providence, Spectral Armor, Nimble Ring, Draconic Scale, Obsidian Shard,
    Leviathan''s Hide, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Stygian Anchor:
      total: 0.65
      efficiency: 0.41
      win: 1.0
      pick: 0.15
      fit: 0.35
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.45
      pick: 0.3
      fit: 0.28
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.28
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Stygian Anchor
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Breastplate of Valor, Nimble Ring, Rod of Tahuti, Kinetic
    Cuirass, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s Garb, Soul Gem, Shield
    of the Phoenix, Spectral Armor, Erosion, Shifter''s Shield, Eye of Providence,
    Draconic Scale, Leviathan''s Hide, Midgardian Mail, Helm of Radiance, Mantle Of
    Discord, Stone of Binding, Death Metal, Screeching Gargoyle, The Cosmic Horror,
    Yogi''s Necklace, Bracer of The Abyss, Rod of Asclepius.'
  slot_scores:
    Stygian Anchor:
      total: 0.64
      efficiency: 0.41
      win: 1.0
      pick: 0.15
      fit: 0.26
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.21
    Bracer of The Abyss:
      total: 0.42
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.49
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.41
      efficiency: 0.42
      win: 0.45
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Kinetic Cuirass, Shield of the Phoenix, Rod of Tahuti, Amanita Charm, Soul Gem,
    Gluttonous Grimoire, Screeching Gargoyle, Chronos'' Pendant, Oni Hunter''s Garb,
    Nimble Ring, Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Erosion,
    Shifter''s Shield, Spectral Armor, Eye of Providence, Prophetic Cloak, Draconic
    Scale, Leviathan''s Hide, Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Stygian Anchor:
      total: 0.65
      efficiency: 0.41
      win: 1.0
      pick: 0.15
      fit: 0.32
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.45
      pick: 0.3
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.48
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.64
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor, Rod
    of Tahuti, The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Gluttonous Grimoire,
    Berserker''s Shield, Amanita Charm, Nimble Ring, Runeforged Hammer, Soul Gem,
    Hydra''s Lament, Shield Splitter, Oni Hunter''s Garb, Shield of the Phoenix, Golden
    Blade, Eye of the Storm, Pharaoh''s Curse, Erosion, Shifter''s Shield, Spectral
    Armor, Eye of Providence, Death Metal, Lernaean Bow, The Reaper, Draconic Scale,
    The Cosmic Horror, Avenging Blade, Damaru, Spear of the Magus, Leviathan''s Hide,
    Shogun''s Ofuda, Midgardian Mail, Spear of Desolation, Mantle Of Discord, Stone
    of Binding, Helm of Radiance, Tekko-Kagi, Screeching Gargoyle.'
  slot_scores:
    Stygian Anchor:
      total: 0.65
      efficiency: 0.41
      win: 1.0
      pick: 0.15
      fit: 0.29
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.45
      pick: 0.3
      fit: 0.23
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.38
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Stygian Anchor
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Breastplate
    of Valor, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Berserker''s Shield, Nimble Ring, Oni Hunter''s Garb,
    The Cosmic Horror, Runeforged Hammer, Shield of the Phoenix, Hydra''s Lament,
    Shield Splitter, Death Metal, Spear of the Magus, Spear of Desolation, Erosion,
    Helm of Radiance, Shifter''s Shield, Eye of the Storm, Spectral Armor, Eye of
    Providence, Draconic Scale, Rod of Asclepius, Chronos'' Pendant, Pharaoh''s Curse,
    The Reaper, Obsidian Shard, Leviathan''s Hide, Golden Blade, Jade Scepter, Midgardian
    Mail, Avenging Blade, Mantle Of Discord, Damaru, Stone of Binding.'
  slot_scores:
    Stygian Anchor:
      total: 0.65
      efficiency: 0.41
      win: 1.0
      pick: 0.15
      fit: 0.29
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.45
      pick: 0.3
      fit: 0.24
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.24
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.45
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Rod of
    Tahuti, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Shifter''s Shield,
    Eye of Providence, Breastplate of Valor, Oni Hunter''s Garb, Draconic Scale, Spectral
    Armor, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail, Stone
    of Binding, Nimble Ring, Gladiator''s Shield, Magi''s Cloak, Screeching Gargoyle,
    Ancile, Prophetic Cloak, Helm of Radiance, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.45
      pick: 0.3
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.75
      pick: 0.11
      fit: 0.65
    Shifter's Shield:
      total: 0.49
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.49
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.7
  starter: *id001
---
