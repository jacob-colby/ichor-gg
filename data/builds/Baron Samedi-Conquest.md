---
type: smite-build
god: Baron Samedi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Hysteria
  aspect_pick_rate: 0.75
  aspect_win_rate: 0.54
  slot_order:
  - name: Lifebinder
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.74
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.86
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.77
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.54
  - name: Ethereal Staff
    pick_rate: 0.11
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.53
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.73
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.63
  - name: Dwarven Plate
    pick_rate: 0.05
    win_rate: 0.25
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.67
  source_url: https://smitebrain.com/gods/baron-samedi/
  last_verified: '2026-08-01'
  god_win_rate: 0.5433526011560693
  god_matches_won: 94
  god_matches_played: 173
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  flex_slots:
  - Breastplate of Valor
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Ethereal Staff, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Eye of Providence, Oni Hunter''s Garb, Shield of the Phoenix, Spectral
    Armor, Freya''s Tears, Wish-Granting Pearl, Shifter''s Shield, Jade Scepter, Spear
    of the Magus, Rod of Asclepius, Mantle Of Discord, Erosion, Yogi''s Necklace,
    Draconic Scale, Helm of Radiance, The Cosmic Horror, Spear of Desolation, Leviathan''s
    Hide, Chronos'' Pendant, Alchemist Coat.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.57
      efficiency: 0.74
      win: 0.56
      pick: 0.2
      fit: 0.31
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.67
      win: 0.55
      pick: 0.17
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.57
      efficiency: 0.7
      win: 0.59
      pick: 0.11
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Ethereal Staff
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Oni Hunter's Garb
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Ethereal Staff, Soul Gem, Kinetic Cuirass, Amanita Charm,
    Oni Hunter''s Garb, Eye of Providence, Shield of the Phoenix, Spear of the Magus,
    Spectral Armor, Death Metal, Freya''s Tears, Wish-Granting Pearl, Yogi''s Necklace,
    Jade Scepter, Mantle Of Discord, Rod of Asclepius, The Cosmic Horror, Shifter''s
    Shield, Spear of Desolation, Triton''s Conch, Erosion, Chronos'' Pendant, Chandra''s
    Grace, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.56
      pick: 0.2
      fit: 0.27
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.17
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.47
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.24
    Ethereal Staff:
      total: 0.55
      efficiency: 0.7
      win: 0.59
      pick: 0.11
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Ethereal Staff, Gluttonous Grimoire, Shield
    of the Phoenix, Rod of Asclepius, Lifebinder, Kinetic Cuirass, Chandra''s Grace,
    Eye of Providence, Oni Hunter''s Garb, Bancroft''s Talon, Blood-Bound Book, Spectral
    Armor, Wish-Granting Pearl, Jade Scepter, Shifter''s Shield, Phoenix Feather,
    Freya''s Tears, Spear of the Magus, Yogi''s Necklace, Erosion, Mantle Of Discord,
    Draconic Scale, Alchemist Coat.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.56
      pick: 0.2
      fit: 0.29
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.17
      fit: 0.29
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.57
      efficiency: 0.7
      win: 0.59
      pick: 0.11
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.79
    Soul Gem:
      total: 0.58
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Kinetic Cuirass
  - Spear of the Magus
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
    for this god: Gluttonous Grimoire, Ethereal Staff, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Spear of the Magus, Eye of Providence, Oni Hunter''s Garb, The
    Cosmic Horror, Spectral Armor, Shield of the Phoenix, Void Shield, Screeching
    Gargoyle, Spear of Desolation, Stone of Binding, Wish-Granting Pearl, Freya''s
    Tears, Obsidian Shard, Jade Scepter, Mantle Of Discord, Shifter''s Shield, Rod
    of Asclepius, Yogi''s Necklace, Void Stone, Erosion.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.56
      pick: 0.2
      fit: 0.26
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.55
      pick: 0.17
      fit: 0.26
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.56
      efficiency: 0.7
      win: 0.59
      pick: 0.11
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of the Magus:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Ethereal Staff
  - Gluttonous Grimoire
  flex_slots:
  - Ethereal Staff
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Eye of Providence, Ethereal Staff, Oni Hunter''s Garb, Shield of the
    Phoenix, Spectral Armor, Freya''s Tears, Wish-Granting Pearl, Shifter''s Shield,
    Jade Scepter, Spear of the Magus, Rod of Asclepius, Mantle Of Discord, Erosion,
    Yogi''s Necklace, Draconic Scale, Helm of Radiance, The Cosmic Horror, Spear of
    Desolation, Leviathan''s Hide, Chronos'' Pendant, Alchemist Coat.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.57
      efficiency: 0.74
      win: 0.56
      pick: 0.2
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.59
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.32
    Ethereal Staff:
      total: 0.57
      efficiency: 0.7
      win: 0.59
      pick: 0.11
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
---
