---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.45
  aspect_win_rate: 0.6
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.3
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.53
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.66
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.56
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.59
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.58
    - name: Soul Gem
      pick_rate: 0.11
      win_rate: 0.63
  - name: Obsidian Shard
    pick_rate: 0.12
    win_rate: 0.43
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.57
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.65
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.43
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.6
    - name: Oracle Staff
      pick_rate: 0.05
      win_rate: 0.44
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.16
    win_rate: 0.51
  - name: Bumba's Cudgel
    pick_rate: 0.12
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-08-22'
  god_win_rate: 0.5723684210526315
  god_matches_won: 261
  god_matches_played: 456
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic Horror,
    The World Stone, Dreamer''s Idol, Nimble Ring, Chronos'' Pendant, Death Metal,
    Gem of Focus, Helm of Radiance, Totem of Death, Breastplate of Valor, Ancient
    Signet, Ethereal Staff, Rod of Asclepius, Jade Scepter, Wish-Granting Pearl, Blood-Bound
    Book, Book of Thoth, Bracer of The Abyss, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.6
      pick: 0.12
      fit: 0.41
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.77
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Doom Orb
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The World Stone
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Gluttonous Grimoire, Spear of the Magus, Doom Orb, Nimble Ring, The World
    Stone, Breastplate of Valor, Ancient Signet, Bragi''s Harp, Chronos'' Pendant,
    The Cosmic Horror, Helm of Radiance, Dreamer''s Idol, Wish-Granting Pearl, Ethereal
    Staff, Book of Thoth, Rod of Asclepius, Triton''s Conch, Gem of Focus, Bancroft''s
    Talon, Polynomicon, Totem of Death, Jade Scepter.'
  slot_scores:
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 0.61
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.57
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.57
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Spear of the Magus, Death Metal, Doom Orb, The Cosmic
    Horror, The World Stone, Breastplate of Valor, Nimble Ring, Dreamer''s Idol, Chronos''
    Pendant, Gem of Focus, Helm of Radiance, Bragi''s Harp, Totem of Death, Ancient
    Signet, Ethereal Staff, Shield of the Phoenix, Rod of Asclepius, Amanita Charm,
    Screeching Gargoyle, Kinetic Cuirass, Jade Scepter, Wish-Granting Pearl.'
  slot_scores:
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 0.78
    Doom Orb:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.56
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.56
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Ethereal
    Staff, Rod of Asclepius, Kinetic Cuirass, Spear of the Magus, Breastplate of Valor,
    Lifebinder, Chandra''s Grace, Blood-Bound Book, Phoenix Feather, Helm of Radiance,
    Nimble Ring, Sphere of Negation, Yogi''s Necklace, Bancroft''s Talon, Erosion,
    Spectral Armor, Eye of Providence, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.42
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 0.5
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.38
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - The Cosmic Horror
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Doom Orb
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The Cosmic Horror,
    The World Stone, Dreamer''s Idol, Nimble Ring, Screeching Gargoyle, Chronos''
    Pendant, Death Metal, Breastplate of Valor, Helm of Radiance, Stone of Binding,
    Ancient Signet, Ethereal Staff, Gem of Focus, Rod of Asclepius, Totem of Death,
    Jade Scepter, Wish-Granting Pearl, Blood-Bound Book, Amanita Charm, Kinetic Cuirass.'
  slot_scores:
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 1.0
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.84
    Doom Orb:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.84
    Spear of the Magus:
      total: 0.61
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.84
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, Spear of the Magus, Death Metal, Bragi''s
    Harp, Breastplate of Valor, Bracer of The Abyss, Helm of Radiance, Doom Orb, The
    Cosmic Horror, Chronos'' Pendant, Amanita Charm, The World Stone, Ancient Signet,
    Kinetic Cuirass, Ethereal Staff, Blood-Bound Book, Dreamer''s Idol, Rod of Asclepius,
    Bancroft''s Talon, Eye of Providence, Gem of Focus, Jade Scepter.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 0.41
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.31
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Chronos'' Pendant,
    Gluttonous Grimoire, Shield of the Phoenix, Gem of Focus, Spear of the Magus,
    Screeching Gargoyle, Totem of Death, Death Metal, Nimble Ring, Chandra''s Grace,
    Doom Orb, The Cosmic Horror, Eye of Erebus, The World Stone, Dreamer''s Idol,
    Helm of Radiance, Amanita Charm, Prophetic Cloak, Kinetic Cuirass, Gladiator''s
    Shield, Ancient Signet, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.16
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.18
      fit: 0.48
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 0.86
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.37
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Death Metal, The Crusher,
    Gluttonous Grimoire, Nimble Ring, Spear of the Magus, Heartseeker, Hydra''s Lament,
    Tyrfing, The Reaper, Bragi''s Harp, Tekko-Kagi, Golden Blade, Lernaean Bow, Runeforged
    Hammer, Titan''s Bane, Berserker''s Shield, Silverbranch Bow, Doom Orb, The Cosmic
    Horror, Riptalon, Breastplate of Valor, The World Stone, Pendulum Blade, Chronos''
    Pendant, Dreamer''s Idol, Arondight, Helm of Radiance, Shield Splitter, Dominance,
    Avatar''s Parashu, Avenging Blade, Triton''s Conch, Bracer of The Abyss, Ancient
    Signet, Ethereal Staff.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.43
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    Death Metal, The Crusher, Spear of the Magus, Heartseeker, The Reaper, Hydra''s
    Lament, Nimble Ring, Doom Orb, The Cosmic Horror, The World Stone, Titan''s Bane,
    Bragi''s Harp, Dreamer''s Idol, Chronos'' Pendant, Runeforged Hammer, Tekko-Kagi,
    Helm of Radiance, Tyrfing, Pendulum Blade, Breastplate of Valor, Golden Blade,
    Ancient Signet, Silverbranch Bow, Ethereal Staff, Triton''s Conch, Rod of Asclepius,
    Arondight, Gem of Focus, Lernaean Bow, Avatar''s Parashu, Riptalon, Berserker''s
    Shield, Shield Splitter, Totem of Death.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.6
      pick: 0.12
      fit: 0.3
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.7
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 0.7
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.55
    Soul Gem:
      total: 0.61
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Doom Orb
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
    Underrated for this god: Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    Cosmic Horror, The World Stone, Dreamer''s Idol, Nimble Ring, Chronos'' Pendant,
    Death Metal, Gem of Focus, Helm of Radiance, Totem of Death, Breastplate of Valor,
    Ancient Signet, Ethereal Staff, Rod of Asclepius, Jade Scepter, Wish-Granting
    Pearl, Blood-Bound Book, Bracer of The Abyss, Bancroft''s Talon, Alchemist Coat,
    Book of Thoth.'
  slot_scores:
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.6
      pick: 0.3
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.6
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.63
      pick: 0.19
      fit: 0.77
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.43
      pick: 0.2
      fit: 0.87
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.63
      pick: 0.17
      fit: 1.0
  starter: *id001
---
