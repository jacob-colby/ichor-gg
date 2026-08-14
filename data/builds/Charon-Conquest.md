---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.47
  slot_order:
  - name: Lifebinder
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.43
    - name: The Cosmic Horror
      pick_rate: 0.1
      win_rate: 0.33
  - name: Totem of Death
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.2
  - name: Omen Drum
    pick_rate: 0.09
    win_rate: 0.4
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 1.0
    - name: The Cosmic Horror
      pick_rate: 0.07
      win_rate: 0.25
  - name: Evil Eye
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.67
  - name: Medallion
    pick_rate: 0.14
    win_rate: 0.75
    alternates:
    - name: Evil Eye
      pick_rate: 0.1
      win_rate: 0.0
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.33
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.45
    win_rate: 0.43
  - name: Bluestone Brooch
    pick_rate: 0.29
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.06
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-13'
  god_win_rate: 0.5161290322580645
  god_matches_won: 32
  god_matches_played: 62
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye
    of Providence, Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s
    Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Screeching Gargoyle, Hide of
    the Nemean Lion, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.18
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.71
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s
    Grace, Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Phoenix
    Feather, Spectral Armor, Leviathan''s Hide, Blood-Bound Book, Bancroft''s Talon,
    Midgardian Mail, Glorious Pridwen, Gladiator''s Shield, Ancile, Jade Scepter,
    Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.18
      fit: 0.7
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.5
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
  - Spear of the Magus
  flex_slots:
  - Stone of Binding
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Freya''s Tears, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Stone of Binding, Spear of the Magus, Screeching Gargoyle, Breastplate
    of Valor, Void Shield, Oni Hunter''s Garb, Shield of the Phoenix, Void Stone,
    Spear of Desolation, Erosion, Obsidian Shard, Eye of Providence, Spectral Armor,
    Draconic Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, The World Stone, The Cosmic Horror.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.41
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Breastplate of Valor, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral
    Armor, Erosion, Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic
    Scale, Leviathan''s Hide, Death Metal, Midgardian Mail, Yogi''s Necklace, Mantle
    Of Discord, Spear of the Magus, Stone of Binding, Blood-Bound Book, Rod of Asclepius,
    Bragi''s Harp, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.2
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire,
    Chronos'' Pendant, Oni Hunter''s Garb, Screeching Gargoyle, Spear of Desolation,
    Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral Armor, Prophetic Cloak,
    Eye of Providence, Draconic Scale, Helm of Radiance, Gem of Focus, Leviathan''s
    Hide, Mantle Of Discord, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.1
      fit: 0.42
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.64
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Breastplate
    of Valor, Soul Gem, Hydra''s Lament, Oni Hunter''s Garb, Runeforged Hammer, Shield
    Splitter, Pharaoh''s Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow,
    Eye of the Storm, Erosion, Death Metal, Spectral Armor, Spear of the Magus, Eye
    of Providence, Shogun''s Ofuda, Damaru, Draconic Scale, The Reaper, Avenging Blade,
    Helm of Radiance, Riptalon, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Silverbranch Bow, Spear of Desolation, Yogi''s
    Necklace, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.47
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s
    Shield, Breastplate of Valor, Spear of the Magus, Oni Hunter''s Garb, Hydra''s
    Lament, Death Metal, Runeforged Hammer, Helm of Radiance, Shield Splitter, Shield
    of the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Eye of the Storm,
    Rod of Asclepius, Eye of Providence, Pharaoh''s Curse, Chronos'' Pendant, Jade
    Scepter, Obsidian Shard, Draconic Scale, Golden Blade, Leviathan''s Hide, Blood-Bound
    Book, Damaru, Lernaean Bow, The Reaper, Bancroft''s Talon, Ethereal Staff, Wish-Granting
    Pearl, Midgardian Mail, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.43
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
    Eye of Providence, Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord,
    Leviathan''s Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s
    Cloak, Gladiator''s Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Screeching
    Gargoyle, Hide of the Nemean Lion, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.56
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.18
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
