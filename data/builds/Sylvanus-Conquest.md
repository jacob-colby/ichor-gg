---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.55
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Tyrfing
      pick_rate: 0.1
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.47
    - name: Circe's Hexstone
      pick_rate: 0.06
      win_rate: 0.38
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.27
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.39
    - name: Regrowth Striders
      pick_rate: 0.05
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.45
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.67
  - name: Mote of Chaos
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.6
  - name: Survivor's Sash
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.28
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.38
  - name: Heroism
    pick_rate: 0.13
    win_rate: 0.69
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-08-13'
  god_win_rate: 0.5161290322580645
  god_matches_won: 64
  god_matches_played: 124
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Oni Hunter's Garb
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Draconic Scale, Shield of the Phoenix, Oni Hunter''s Garb, Erosion, Soul Gem,
    Eye of Providence, Spectral Armor, Helm of Radiance, Leviathan''s Hide, Mantle
    Of Discord, Stone of Binding, Midgardian Mail, Rod of Asclepius, Screeching Gargoyle,
    Gladiator''s Shield, Magi''s Cloak, Jade Scepter, Prophetic Cloak, Chronos'' Pendant,
    Spear of the Magus, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.62
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.6
      pick: 0.11
      fit: 0.63
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.63
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
  - Kinetic Cuirass
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Soul Gem, Kinetic
    Cuirass, Gluttonous Grimoire, Rod of Asclepius, Draconic Scale, Chandra''s Grace,
    Oni Hunter''s Garb, Erosion, Blood-Bound Book, Eye of Providence, Bancroft''s
    Talon, Phoenix Feather, Spectral Armor, Lifebinder, Glorious Pridwen, Leviathan''s
    Hide, Helm of Radiance, Jade Scepter, Midgardian Mail, Gladiator''s Shield, Chronos''
    Pendant, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.36
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.55
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.6
      pick: 0.11
      fit: 0.62
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Stone of Binding
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Gluttonous Grimoire, Freya''s Tears, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Stone of Binding, Spear of the Magus, Screeching Gargoyle, The
    Cosmic Horror, Draconic Scale, Spear of Desolation, Void Shield, Oni Hunter''s
    Garb, Shield of the Phoenix, Void Stone, Obsidian Shard, Erosion, Spectral Armor,
    Eye of Providence, Helm of Radiance, The World Stone, Leviathan''s Hide, Doom
    Orb, Rod of Asclepius, Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.28
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Oni Hunter''s Garb, Draconic Scale, Shield of the Phoenix, Spectral
    Armor, Bracer of The Abyss, Erosion, Helm of Radiance, Eye of Providence, Death
    Metal, Spear of the Magus, Blood-Bound Book, Leviathan''s Hide, Rod of Asclepius,
    Bancroft''s Talon, Yogi''s Necklace, Bragi''s Harp, Midgardian Mail, Jade Scepter,
    The Cosmic Horror, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.21
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Draconic Scale
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Shield
    of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Draconic Scale,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation,
    Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence,
    Prophetic Cloak, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of
    Discord, Midgardian Mail, Rod of Asclepius, Stone of Binding, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.22
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
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.64
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.6
      pick: 0.11
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire, Jotunn''s
    Revenge, Berserker''s Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Soul
    Gem, Hydra''s Lament, Oni Hunter''s Garb, Draconic Scale, Runeforged Hammer, Shield
    Splitter, Shield of the Phoenix, Pharaoh''s Curse, Golden Blade, Lernaean Bow,
    Death Metal, Spear of the Magus, Eye of the Storm, Spectral Armor, Erosion, The
    Cosmic Horror, Helm of Radiance, Eye of Providence, Damaru, Shogun''s Ofuda, The
    Reaper, Spear of Desolation, Avenging Blade, Riptalon, Leviathan''s Hide, Rod
    of Asclepius, Midgardian Mail, Mantle Of Discord, Bragi''s Harp, Stone of Binding,
    Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.24
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Jotunn''s Revenge, Soul Gem, Kinetic Cuirass, The Crusher, Amanita Charm, Berserker''s
    Shield, Hydra''s Lament, Spear of the Magus, Draconic Scale, Oni Hunter''s Garb,
    Death Metal, Shield of the Phoenix, The Cosmic Horror, Runeforged Hammer, Helm
    of Radiance, Shield Splitter, Spear of Desolation, Spectral Armor, Erosion, Rod
    of Asclepius, Eye of the Storm, Pharaoh''s Curse, Eye of Providence, Obsidian
    Shard, Jade Scepter, Chronos'' Pendant, Golden Blade, Leviathan''s Hide, Blood-Bound
    Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle
    Of Discord, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Freya''s Tears, Breastplate of Valor, Shield of the Phoenix, Oni Hunter''s Garb,
    Erosion, Soul Gem, Eye of Providence, Draconic Scale, Spectral Armor, Helm of
    Radiance, Leviathan''s Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail,
    Rod of Asclepius, Screeching Gargoyle, Gladiator''s Shield, Magi''s Cloak, Jade
    Scepter, Prophetic Cloak, Chronos'' Pendant, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.39
    Breastplate of Valor:
      total: 0.42
      efficiency: 0.66
      win: 0.27
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.63
  starter: *id001
---
