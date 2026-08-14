---
type: smite-build
god: Sobek
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prey
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.24
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.29
    win_rate: 0.62
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.45
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.63
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.58
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.52
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.07
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.65
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.53
  - name: Veve Charm
    pick_rate: 0.06
    win_rate: 0.73
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.35
    win_rate: 0.53
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.54
  - name: Selflessness
    pick_rate: 0.12
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/sobek/
  last_verified: '2026-08-14'
  god_win_rate: 0.5306122448979592
  god_matches_won: 182
  god_matches_played: 343
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
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
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
    this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Breastplate of
    Valor, Freya''s Tears, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye
    of Providence, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s Hide,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Hide of the Nemean
    Lion, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.26
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.64
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Oni Hunter's Garb
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Breastplate
    of Valor, Eye of Providence, Phoenix Feather, Freya''s Tears, Spectral Armor,
    Leviathan''s Hide, Blood-Bound Book, Lifebinder, Bancroft''s Talon, Midgardian
    Mail, Glorious Pridwen, Gladiator''s Shield, Ancile, Jade Scepter, Void Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.92
    Oni Hunter's Garb:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Draconic Scale
  - Spear of the Magus
  flex_slots:
  - Spear of the Magus
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita Charm, Stone
    of Binding, Spear of the Magus, Screeching Gargoyle, Breastplate of Valor, Void
    Shield, The Cosmic Horror, Oni Hunter''s Garb, Void Stone, Shield of the Phoenix,
    Spear of Desolation, Freya''s Tears, Erosion, Obsidian Shard, Eye of Providence,
    Spectral Armor, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, The World Stone.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.26
      fit: 0.27
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.66
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.49
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Breastplate of
    Valor, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Freya''s Tears, Spectral
    Armor, Erosion, Bracer of The Abyss, Eye of Providence, Helm of Radiance, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Yogi''s Necklace, Mantle Of Discord, Stone
    of Binding, Spear of the Magus, Rod of Asclepius, Blood-Bound Book, Bragi''s Harp,
    Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.26
      fit: 0.2
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.35
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
  - Freya's Tears
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Kinetic Cuirass,
    Shield of the Phoenix, Soul Gem, Amanita Charm, Freya''s Tears, Gluttonous Grimoire,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation,
    Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence,
    Prophetic Cloak, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of
    Discord, Midgardian Mail, Rod of Asclepius, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.64
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix,
    Eye of Providence, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s Hide,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Hide of the Nemean
    Lion, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.26
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.5
      efficiency: 0.52
      win: 0.45
      pick: 0.19
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.71
  starter: *id001
---
