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
  - Eye of Providence
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Ethereal Staff, Kinetic Cuirass, Eye of Providence,
    Amanita Charm, Spear of the Magus, Soul Gem, Spectral Armor, Rod of Asclepius,
    Lifebinder, Shield of the Phoenix, Erosion, Obsidian Shard, The Cosmic Horror,
    Chandra''s Grace, Helm of Radiance, Chronos'' Pendant, Blood-Bound Book, Alchemist
    Coat, Spear of Desolation, Gladiator''s Shield, Jade Scepter, Midgardian Mail,
    Bancroft''s Talon, Ancient Signet.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.56
      pick: 0.2
      fit: 0.31
    Breastplate of Valor:
      total: 0.45
      efficiency: 0.42
      win: 0.55
      pick: 0.17
      fit: 0.31
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.49
      efficiency: 0.47
      win: 0.59
      pick: 0.11
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Eye of Providence
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Ethereal Staff, Kinetic Cuirass, Eye of Providence,
    Spear of the Magus, Soul Gem, Amanita Charm, Spectral Armor, Obsidian Shard, Rod
    of Asclepius, Shield of the Phoenix, The Cosmic Horror, Death Metal, Erosion,
    Chandra''s Grace, Spear of Desolation, Chronos'' Pendant, Blood-Bound Book, Helm
    of Radiance, Triton''s Conch, Gladiator''s Shield, Bragi''s Harp, Alchemist Coat,
    Bancroft''s Talon, Ancient Signet.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.56
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Ethereal Staff:
      total: 0.47
      efficiency: 0.47
      win: 0.59
      pick: 0.11
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.48
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Ethereal Staff, Rod of Asclepius,
    Soul Gem, Lifebinder, Shield of the Phoenix, Chandra''s Grace, Kinetic Cuirass,
    Eye of Providence, Blood-Bound Book, Bancroft''s Talon, Phoenix Feather, Spear
    of the Magus, Spectral Armor, Erosion, Obsidian Shard, Spirit Robe, The Cosmic
    Horror, Alchemist Coat, Chronos'' Pendant, Gladiator''s Shield, Helm of Radiance,
    Jade Scepter, Spear of Desolation.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.56
      pick: 0.2
      fit: 0.29
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.49
      efficiency: 0.47
      win: 0.59
      pick: 0.11
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Ethereal Staff, Spear of the Magus, Soul Gem,
    Kinetic Cuirass, Eye of Providence, Obsidian Shard, Amanita Charm, Screeching
    Gargoyle, The Cosmic Horror, Spectral Armor, Rod of Asclepius, Lifebinder, Void
    Stone, Spear of Desolation, Void Shield, Stone of Binding, Shield of the Phoenix,
    Erosion, Chandra''s Grace, Blood-Bound Book, Helm of Radiance, Chronos'' Pendant,
    Alchemist Coat, Doom Orb.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.41
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.56
      pick: 0.2
      fit: 0.26
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.51
    Ethereal Staff:
      total: 0.48
      efficiency: 0.47
      win: 0.59
      pick: 0.11
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of the Magus:
      total: 0.46
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.22
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.24
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - Spear of the Magus
  - Spectral Armor
  flex_slots:
  - Spectral Armor
  - Ethereal Staff
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
    Underrated for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence,
    Amanita Charm, Spear of the Magus, Soul Gem, Spectral Armor, Ethereal Staff, Rod
    of Asclepius, Shield of the Phoenix, Erosion, Obsidian Shard, The Cosmic Horror,
    Chandra''s Grace, Helm of Radiance, Chronos'' Pendant, Blood-Bound Book, Alchemist
    Coat, Spear of Desolation, Gladiator''s Shield, Lifebinder, Jade Scepter, Midgardian
    Mail, Bancroft''s Talon, Ancient Signet.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.49
      efficiency: 0.47
      win: 0.59
      pick: 0.11
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.49
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of the Magus:
      total: 0.45
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.37
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
  starter: *id001
---
