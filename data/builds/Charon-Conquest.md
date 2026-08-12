---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.54
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Lifebinder
      pick_rate: 0.15
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.47
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.3
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.65
  - name: Ethereal Staff
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.44
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.5
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.42
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.41
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.58
  - name: War Banner
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-11'
  god_win_rate: 0.5214067278287462
  god_matches_won: 341
  god_matches_played: 654
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Breastplate of Valor,
    Eye of Providence, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of
    the Phoenix, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide, Mantle
    Of Discord, Stone of Binding, Midgardian Mail, Yogi''s Necklace, Hide of the Nemean
    Lion, Helm of Radiance, Rod of Asclepius, Magi''s Cloak, Stampede, Ancile, Gladiator''s
    Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.71
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.13
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.81
    Ethereal Staff:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.06
      fit: 0.3
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Ethereal Staff
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Eye of Providence, Breastplate of Valor, Soul Gem, Gluttonous Grimoire, Rod of
    Asclepius, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Draconic Scale, Phoenix
    Feather, Spectral Armor, Lifebinder, Yogi''s Necklace, Leviathan''s Hide, Blood-Bound
    Book, Midgardian Mail, Bancroft''s Talon, Hide of the Nemean Lion, Glorious Pridwen,
    Jade Scepter, Stampede.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Ethereal Staff:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.06
      fit: 0.36
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.57
    Amanita Charm:
      total: 0.61
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Ethereal Staff
  - Eye of Providence
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Breastplate of Valor, Amanita
    Charm, Kinetic Cuirass, Soul Gem, Eye of Providence, Stone of Binding, Oni Hunter''s
    Garb, Spear of the Magus, Screeching Gargoyle, Void Shield, The Cosmic Horror,
    Shield of the Phoenix, Void Stone, Spear of Desolation, Erosion, Spectral Armor,
    Draconic Scale, Obsidian Shard, Yogi''s Necklace, Leviathan''s Hide, Helm of Radiance,
    Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.49
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.13
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.06
      fit: 0.2
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Breastplate of Valor, Amanita Charm, Gluttonous Grimoire,
    Kinetic Cuirass, Eye of Providence, Oni Hunter''s Garb, Soul Gem, Shield of the
    Phoenix, Spectral Armor, Yogi''s Necklace, Erosion, Bracer of The Abyss, Death
    Metal, Draconic Scale, Rod of Asclepius, Helm of Radiance, Leviathan''s Hide,
    Bragi''s Harp, Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus, Jade
    Scepter, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.13
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
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.44
    Ethereal Staff:
      total: 0.51
      efficiency: 0.53
      win: 0.67
      pick: 0.06
      fit: 0.15
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Gluttonous Grimoire,
    Eye of Providence, Oni Hunter''s Garb, Prophetic Cloak, Chronos'' Pendant, Screeching
    Gargoyle, Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Spectral
    Armor, Erosion, Yogi''s Necklace, Draconic Scale, Helm of Radiance, Rod of Asclepius,
    Gem of Focus, Death Metal, Leviathan''s Hide, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.17
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.57
      pick: 0.13
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Ethereal Staff:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.06
      fit: 0.22
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
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
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor, Berserker''s
    Shield, The Crusher, Jotunn''s Revenge, Gluttonous Grimoire, Amanita Charm, Kinetic
    Cuirass, Eye of Providence, Runeforged Hammer, Hydra''s Lament, Oni Hunter''s
    Garb, Shield Splitter, Soul Gem, Golden Blade, Lernaean Bow, Eye of the Storm,
    Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral Armor, Avenging
    Blade, Erosion, Yogi''s Necklace, The Reaper, Damaru, Spear of the Magus, Draconic
    Scale, Shogun''s Ofuda, Leviathan''s Hide, The Cosmic Horror, Helm of Radiance,
    Rod of Asclepius, Dominance, Heartseeker, Riptalon, Midgardian Mail, Bragi''s
    Harp.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.13
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Ethereal Staff
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Breastplate of Valor, Amanita Charm, The Crusher, Jotunn''s Revenge, Kinetic Cuirass,
    Berserker''s Shield, Soul Gem, Eye of Providence, Runeforged Hammer, Oni Hunter''s
    Garb, Hydra''s Lament, Death Metal, Spear of the Magus, Shield Splitter, The Cosmic
    Horror, Helm of Radiance, Shield of the Phoenix, Rod of Asclepius, Eye of the
    Storm, Spectral Armor, Erosion, Spear of Desolation, Jade Scepter, Yogi''s Necklace,
    Pharaoh''s Curse, Avenging Blade, Draconic Scale, Golden Blade, Obsidian Shard,
    Lernaean Bow, The Reaper, Triton''s Conch, Chronos'' Pendant, Damaru, Leviathan''s
    Hide, Wish-Granting Pearl.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.13
      fit: 0.23
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Ethereal Staff:
      total: 0.54
      efficiency: 0.53
      win: 0.67
      pick: 0.06
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Freya''s
    Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of the Phoenix,
    Breastplate of Valor, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, Yogi''s Necklace, Hide of
    the Nemean Lion, Helm of Radiance, Rod of Asclepius, Magi''s Cloak, Stampede,
    Ancile, Gladiator''s Shield, Hussar''s Wings.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.17
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.05
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.19
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
