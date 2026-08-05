---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.6
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.26
    win_rate: 0.58
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.17
      win_rate: 0.65
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.16
      win_rate: 0.63
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.7
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.81
    alternates:
    - name: Genji's Guard
      pick_rate: 0.24
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.45
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.36
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.57
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.5
  - name: Ethereal Staff
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.22
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.38
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.88
    alternates:
    - name: Medallion
      pick_rate: 0.07
      win_rate: 0.5
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-01'
  god_win_rate: 0.5570469798657718
  god_matches_won: 83
  god_matches_played: 149
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Ethereal Staff, Kinetic Cuirass, Amanita Charm,
    Eye of Providence, Gluttonous Grimoire, Oni Hunter''s Garb, Freya''s Tears, Shield
    of the Phoenix, Erosion, Spectral Armor, Draconic Scale, Mantle Of Discord, Leviathan''s
    Hide, Hussar''s Wings, Soul Gem, Yogi''s Necklace, Midgardian Mail, Hide of the
    Nemean Lion, Wish-Granting Pearl, Doublet of Binding, Jade Scepter, Gladiator''s
    Shield, Rod of Asclepius, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.39
    Breastplate of Valor:
      total: 0.67
      efficiency: 0.67
      win: 0.81
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.81
    Ethereal Staff:
      total: 0.6
      efficiency: 0.7
      win: 0.67
      pick: 0.1
      fit: 0.3
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.58
      pick: 0.26
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
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
  - Breastplate of Valor
  - Shield of the Phoenix
  - Ethereal Staff
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Ethereal Staff, Shield of the Phoenix,
    Kinetic Cuirass, Eye of Providence, Gluttonous Grimoire, Soul Gem, Rod of Asclepius,
    Oni Hunter''s Garb, Chandra''s Grace, Spectral Armor, Erosion, Draconic Scale,
    Phoenix Feather, Freya''s Tears, Lifebinder, Mantle Of Discord, Yogi''s Necklace,
    Leviathan''s Hide, Bancroft''s Talon, Blood-Bound Book, Wish-Granting Pearl, Spirit
    Robe, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.36
    Breastplate of Valor:
      total: 0.66
      efficiency: 0.67
      win: 0.81
      pick: 0.14
      fit: 0.36
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.92
    Ethereal Staff:
      total: 0.61
      efficiency: 0.7
      win: 0.67
      pick: 0.1
      fit: 0.36
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.58
      pick: 0.26
      fit: 0.7
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, Ethereal Staff, Gluttonous Grimoire, Kinetic
    Cuirass, Amanita Charm, Soul Gem, Eye of Providence, Oni Hunter''s Garb, Stone
    of Binding, Spectral Armor, Void Shield, Spear of the Magus, Shield of the Phoenix,
    Freya''s Tears, Mantle Of Discord, Screeching Gargoyle, Erosion, Void Stone, The
    Cosmic Horror, Draconic Scale, Yogi''s Necklace, Spear of Desolation, Leviathan''s
    Hide, Wish-Granting Pearl, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.27
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.67
      win: 0.81
      pick: 0.14
      fit: 0.27
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.58
      efficiency: 0.7
      win: 0.67
      pick: 0.1
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.58
      pick: 0.26
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Ethereal Staff, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Oni Hunter''s Garb, Eye of Providence, Spectral Armor, Soul Gem,
    Shield of the Phoenix, Mantle Of Discord, Yogi''s Necklace, Freya''s Tears, Bracer
    of The Abyss, Bragi''s Harp, Erosion, Death Metal, Draconic Scale, Wish-Granting
    Pearl, Leviathan''s Hide, Jade Scepter, Rod of Asclepius, Nimble Ring, Midgardian
    Mail, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.2
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.67
      win: 0.81
      pick: 0.14
      fit: 0.2
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Ethereal Staff:
      total: 0.57
      efficiency: 0.7
      win: 0.67
      pick: 0.1
      fit: 0.15
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Ethereal Staff
  - Shifter's Shield
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Ethereal Staff,
    Kinetic Cuirass, Shield of the Phoenix, Amanita Charm, Gluttonous Grimoire, Freya''s
    Tears, Soul Gem, Eye of Providence, Oni Hunter''s Garb, Chandra''s Grace, Spectral
    Armor, Chronos'' Pendant, Mantle Of Discord, Gladiator''s Shield, Erosion, Yogi''s
    Necklace, Screeching Gargoyle, Draconic Scale, Wish-Granting Pearl, Jade Scepter,
    Death Metal, Leviathan''s Hide, Rod of Asclepius, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.48
    Breastplate of Valor:
      total: 0.68
      efficiency: 0.67
      win: 0.81
      pick: 0.14
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Ethereal Staff:
      total: 0.59
      efficiency: 0.7
      win: 0.67
      pick: 0.1
      fit: 0.22
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.26
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Ethereal Staff
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
  - Gluttonous Grimoire
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Breastplate of Valor, Ethereal Staff, The
    Crusher, Gluttonous Grimoire, Berserker''s Shield, Jotunn''s Revenge, Runeforged
    Hammer, Kinetic Cuirass, Hydra''s Lament, Amanita Charm, Eye of Providence, Lernaean
    Bow, Oni Hunter''s Garb, Avenging Blade, Golden Blade, Shield Splitter, Pharaoh''s
    Curse, Eye of the Storm, Soul Gem, Spectral Armor, Death Metal, Shield of the
    Phoenix, Mantle Of Discord, Freya''s Tears, Damaru, The Reaper, Yogi''s Necklace,
    Erosion, Heartseeker, Draconic Scale, Bragi''s Harp, Shogun''s Ofuda, Triton''s
    Conch, Leviathan''s Hide, Arondight, Wish-Granting Pearl, Avatar''s Parashu.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.23
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.67
      win: 0.81
      pick: 0.14
      fit: 0.23
    Ethereal Staff:
      total: 0.58
      efficiency: 0.7
      win: 0.67
      pick: 0.1
      fit: 0.17
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.42
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.26
      fit: 0.41
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Ethereal Staff
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Ethereal Staff,
    Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Runeforged Hammer, Kinetic
    Cuirass, Amanita Charm, Berserker''s Shield, Hydra''s Lament, Soul Gem, Eye of
    Providence, Oni Hunter''s Garb, Death Metal, Avenging Blade, Shield Splitter,
    Spectral Armor, Eye of the Storm, Wish-Granting Pearl, Lernaean Bow, Shield of
    the Phoenix, Jade Scepter, Mantle Of Discord, Triton''s Conch, Spear of the Magus,
    Freya''s Tears, Rod of Asclepius, Pharaoh''s Curse, Golden Blade, Yogi''s Necklace,
    Erosion, Helm of Radiance, Damaru, The Reaper, Draconic Scale, The Cosmic Horror,
    Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.23
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.67
      win: 0.81
      pick: 0.14
      fit: 0.23
    Ethereal Staff:
      total: 0.6
      efficiency: 0.7
      win: 0.67
      pick: 0.1
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.26
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.7
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
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Oni Hunter''s Garb, Freya''s Tears, Shield of the Phoenix, Erosion,
    Spectral Armor, Draconic Scale, Mantle Of Discord, Breastplate of Valor, Ethereal
    Staff, Leviathan''s Hide, Hussar''s Wings, Soul Gem, Yogi''s Necklace, Midgardian
    Mail, Hide of the Nemean Lion, Wish-Granting Pearl, Doublet of Binding, Jade Scepter,
    Gladiator''s Shield, Rod of Asclepius, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Genji's Guard:
      total: 0.58
      efficiency: 0.74
      win: 0.56
      pick: 0.17
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.81
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.58
      pick: 0.26
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
