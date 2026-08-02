---
type: smite-build
god: Janus
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.5
    win_rate: 0.48
    alternates:
    - name: Book of Thoth
      pick_rate: 0.35
      win_rate: 0.55
    - name: Doom Orb
      pick_rate: 0.05
      win_rate: 0.57
  - name: Book of Thoth
    pick_rate: 0.25
    win_rate: 0.48
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.27
      win_rate: 0.54
    - name: Soul Gem
      pick_rate: 0.14
      win_rate: 0.55
  - name: Soul Gem
    pick_rate: 0.42
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.55
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.41
  - name: Rod of Tahuti
    pick_rate: 0.39
    win_rate: 0.48
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.23
      win_rate: 0.54
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.52
  - name: Obsidian Shard
    pick_rate: 0.3
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.6
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.39
  - name: Blinking Abyss
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.63
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.4
  source_url: https://smitebrain.com/gods/janus/
  last_verified: '2026-08-01'
  god_win_rate: 0.4982638888888889
  god_matches_won: 287
  god_matches_played: 576
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
  - Chronos' Pendant
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Chronos''
    Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Doom Orb, Bancroft''s
    Talon, Ancient Signet, Gem of Focus, Death Metal, The World Stone, Polynomicon,
    Helm of Radiance, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s Harp, Jade
    Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Chronos' Pendant:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.67
    Spear of Desolation:
      total: 0.5
      efficiency: 0.32
      win: 0.48
      pick: 0.5
      fit: 1.0
    The Cosmic Horror:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spear of the Magus:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.78
    Obsidian Shard:
      total: 0.51
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.78
    Soul Gem:
      total: 0.55
      efficiency: 0.36
      win: 0.56
      pick: 0.42
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Death Metal,
    Chronos'' Pendant, Bragi''s Harp, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Genji''s Guard, Doom Orb, Bancroft''s Talon, Ancient Signet, Triton''s Conch,
    Gem of Focus, Chandra''s Grace, Breastplate of Valor, The World Stone, Shield
    of the Phoenix, Polynomicon, Helm of Radiance, Spectral Armor, Alchemist Coat.'
  slot_scores:
    Death Metal:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.47
      efficiency: 0.32
      win: 0.48
      pick: 0.5
      fit: 0.78
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.47
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.56
    Obsidian Shard:
      total: 0.48
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.56
    Soul Gem:
      total: 0.53
      efficiency: 0.36
      win: 0.56
      pick: 0.42
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Ethereal Staff
  - Spectral Armor
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Ethereal Staff
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
    this god: Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Shield of the
    Phoenix, Kinetic Cuirass, Eye of Providence, Chandra''s Grace, Lifebinder, Blood-Bound
    Book, Bancroft''s Talon, Phoenix Feather, Spectral Armor, Ethereal Staff, Spear
    of the Magus, Erosion, Spirit Robe, Genji''s Guard, Alchemist Coat, The Cosmic
    Horror, Helm of Radiance, Jade Scepter, Midgardian Mail, Gladiator''s Shield,
    Chronos'' Pendant, Breastplate of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.52
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Ethereal Staff:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.82
    Soul Gem:
      total: 0.53
      efficiency: 0.36
      win: 0.56
      pick: 0.42
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror, Doom
    Orb, The World Stone, Ethereal Staff, Chronos'' Pendant, Rod of Asclepius, Blood-Bound
    Book, Screeching Gargoyle, Bancroft''s Talon, Ancient Signet, Death Metal, Dreamer''s
    Idol, Gem of Focus, Polynomicon, Helm of Radiance, Genji''s Guard, Alchemist Coat,
    Divine Ruin, Lifebinder, Bragi''s Harp.'
  slot_scores:
    Spear of Desolation:
      total: 0.5
      efficiency: 0.32
      win: 0.48
      pick: 0.5
      fit: 1.0
    The Cosmic Horror:
      total: 0.49
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.85
    Doom Orb:
      total: 0.46
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.85
    Spear of the Magus:
      total: 0.52
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.85
    Obsidian Shard:
      total: 0.52
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.85
    Soul Gem:
      total: 0.55
      efficiency: 0.36
      win: 0.56
      pick: 0.42
      fit: 1.0
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
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - The Cosmic Horror
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, The Cosmic Horror,
    Chronos'' Pendant, Ethereal Staff, Rod of Asclepius, Blood-Bound Book, Doom Orb,
    Bancroft''s Talon, Ancient Signet, Gem of Focus, Death Metal, The World Stone,
    Polynomicon, Helm of Radiance, Alchemist Coat, Divine Ruin, Lifebinder, Bragi''s
    Harp, Jade Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Chronos' Pendant:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.67
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.88
    Spear of Desolation:
      total: 0.5
      efficiency: 0.32
      win: 0.48
      pick: 0.5
      fit: 1.0
    The Cosmic Horror:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spear of the Magus:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.78
    Obsidian Shard:
      total: 0.51
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Ethereal Staff
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - The Cosmic Horror
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Spear of the
    Magus, The Cosmic Horror, Chronos'' Pendant, Ethereal Staff, Rod of Asclepius,
    Blood-Bound Book, Doom Orb, Bancroft''s Talon, Ancient Signet, Gem of Focus, Death
    Metal, The World Stone, Polynomicon, Helm of Radiance, Alchemist Coat, Divine
    Ruin, Lifebinder, Bragi''s Harp, Jade Scepter, Genji''s Guard, Scepter of Dominion.'
  slot_scores:
    Ethereal Staff:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.5
      efficiency: 0.32
      win: 0.48
      pick: 0.5
      fit: 1.0
    The Cosmic Horror:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spear of the Magus:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.78
    Obsidian Shard:
      total: 0.51
      efficiency: 0.41
      win: 0.52
      pick: 0.3
      fit: 0.78
    Soul Gem:
      total: 0.55
      efficiency: 0.36
      win: 0.56
      pick: 0.42
      fit: 1.0
  swaps:
  - added: Soul Gem
    removed: Chronos' Pendant
    reason: community 56% win over 242 matches (vs 50% on this god), taking the model's
      weakest slot from Chronos' Pendant
  starter: *id001
---
