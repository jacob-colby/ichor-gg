---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.47
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.42
    win_rate: 0.66
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.24
      win_rate: 0.56
    - name: Transcendence
      pick_rate: 0.06
      win_rate: 0.2
  - name: Sanguine Lash
    pick_rate: 0.17
    win_rate: 0.62
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.22
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.57
  - name: Sundering Echo
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.61
    - name: Umbral Link
      pick_rate: 0.05
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.05
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.75
    - name: Sundering Echo
      pick_rate: 0.07
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Sundering Echo
      pick_rate: 0.06
      win_rate: 0.78
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.43
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.49
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.23
    win_rate: 0.41
  - name: Archmage's Gem
    pick_rate: 0.08
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-11-08'
  god_win_rate: 0.5497835497835498
  god_matches_won: 127
  god_matches_played: 231
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Genji''s Guard, Amanita Charm, Kinetic
    Cuirass, Jotunn''s Revenge, Gluttonous Grimoire, Shield Splitter, Golden Blade,
    Runeforged Hammer, Tyrfing, The Reaper, Soul Gem, Oni Hunter''s Garb, Hydra''s
    Lament, Shield of the Phoenix, Draconic Scale, Breastplate of Valor, Avenging
    Blade, Death Metal, Bragi''s Harp, Nimble Ring, Blood-Bound Book, Erosion, Eye
    of Providence, Midgardian Mail, The Crusher, Spear of Desolation, Leviathan''s
    Hide, Wyrmskin Hide, Lernaean Bow, Dominance, Heartseeker, Hide of the Nemean
    Lion, Tekko-Kagi, Shogun''s Ofuda, Pharaoh''s Curse, Triton''s Conch, Helm of
    Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.64
      pick: 0.11
      fit: 0.15
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.33
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.69
      pick: 0.34
      fit: 0.26
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Genji''s Guard, Kinetic Cuirass,
    Shield of the Phoenix, Rod of Tahuti, Soul Gem, The Reaper, Blood-Bound Book,
    Shield Splitter, Phoenix Feather, Gluttonous Grimoire, Jotunn''s Revenge, Yogi''s
    Necklace, Runeforged Hammer, Ethereal Staff, Golden Blade, Draconic Scale, Tyrfing,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Bloodforge, Bancroft''s Talon,
    Breastplate of Valor, Chandra''s Grace, Riptalon, Midgardian Mail, Hydra''s Lament,
    Leviathan''s Hide, Hide of the Nemean Lion, Avenging Blade, Regrowth Striders,
    Shogun''s Ofuda, Wyrmskin Hide, Pharaoh''s Curse, Death Metal, Nimble Ring, Stone
    of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.64
      pick: 0.11
      fit: 0.18
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.69
      pick: 0.34
      fit: 0.33
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.79
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, Genji''s Guard, Soul Gem, The Reaper, Amanita Charm, Kinetic Cuirass,
    Avenging Blade, Spear of Desolation, The Crusher, Heartseeker, Screeching Gargoyle,
    Stone of Binding, Tekko-Kagi, Titan''s Bane, Obsidian Shard, Void Stone, Void
    Shield, Shield Splitter, Runeforged Hammer, Toxic Blade, Tyrfing, Spear of the
    Magus, Golden Blade, Dreamer''s Idol, Silverbranch Bow, Breastplate of Valor,
    Oni Hunter''s Garb, Riptalon, Hydra''s Lament, Shield of the Phoenix, Avatar''s
    Parashu, Doom Orb, Blood-Bound Book, Draconic Scale, Death Metal, Nimble Ring,
    The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.64
      pick: 0.11
      fit: 0.11
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.69
      pick: 0.34
      fit: 0.19
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.59
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Genji''s Guard, Amanita Charm, Tyrfing,
    Golden Blade, Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, Nimble
    Ring, Soul Gem, Toxic Blade, Shield Splitter, Runeforged Hammer, Bragi''s Harp,
    Breastplate of Valor, Oni Hunter''s Garb, Shogun''s Ofuda, Pharaoh''s Curse, Lernaean
    Bow, The Reaper, Dominance, Silverbranch Bow, Shield of the Phoenix, Riptalon,
    Tekko-Kagi, Blood-Bound Book, Hydra''s Lament, Draconic Scale, Qin''s Blade, Spear
    of Desolation, Midgardian Mail, Bracer of The Abyss, Erosion, Death Metal, Ancient
    Signet, Leviathan''s Hide, Eye of Providence, Helm of Radiance, Hide of the Nemean
    Lion.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.64
      pick: 0.11
      fit: 0.11
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.69
      pick: 0.34
      fit: 0.19
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.59
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Jotunn's Revenge
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Soul
    Gem, Jotunn''s Revenge, Berserker''s Shield, Breastplate of Valor, Amanita Charm,
    Spear of Desolation, Shield of the Phoenix, Kinetic Cuirass, Hydra''s Lament,
    Gluttonous Grimoire, Screeching Gargoyle, Chronos'' Pendant, Arondight, Gladiator''s
    Shield, Shield Splitter, Blood-Bound Book, Runeforged Hammer, Gem of Focus, Heartwood
    Charm, Tyrfing, Oni Hunter''s Garb, Chandra''s Grace, Nimble Ring, Golden Blade,
    The Reaper, Eye of Erebus, Ancient Signet, Helm of Radiance, Draconic Scale, Prophetic
    Cloak, Damaru, Death Metal, Midgardian Mail, Polynomicon, Regrowth Striders, Erosion,
    Obsidian Shard, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.64
      pick: 0.11
      fit: 0.4
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.59
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.69
      pick: 0.34
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.45
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Jotunn''s Revenge, Gluttonous Grimoire, Genji''s Guard, Shield Splitter,
    Golden Blade, Runeforged Hammer, Tyrfing, The Reaper, Soul Gem, Oni Hunter''s
    Garb, Hydra''s Lament, Shield of the Phoenix, Draconic Scale, Breastplate of Valor,
    Avenging Blade, Death Metal, Bragi''s Harp, Nimble Ring, Blood-Bound Book, Erosion,
    Eye of Providence, Midgardian Mail, The Crusher, Spear of Desolation, Leviathan''s
    Hide, Wyrmskin Hide, Lernaean Bow, Dominance, Heartseeker, Hide of the Nemean
    Lion, Tekko-Kagi, Shogun''s Ofuda, Pharaoh''s Curse, Triton''s Conch, Helm of
    Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.64
      pick: 0.11
      fit: 0.15
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.33
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.59
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Kinetic Cuirass
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Devourer's Gauntlet
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Rod of Tahuti,
    Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Gluttonous Grimoire, Genji''s
    Guard, Shield Splitter, Golden Blade, Runeforged Hammer, Tyrfing, The Reaper,
    Soul Gem, Oni Hunter''s Garb, Hydra''s Lament, Shield of the Phoenix, Draconic
    Scale, Breastplate of Valor, Avenging Blade, Death Metal, Bragi''s Harp, Nimble
    Ring, Blood-Bound Book, Erosion, Eye of Providence, Midgardian Mail, The Crusher,
    Spear of Desolation, Leviathan''s Hide, Wyrmskin Hide, Lernaean Bow, Dominance,
    Heartseeker, Hide of the Nemean Lion, Tekko-Kagi, Shogun''s Ofuda, Pharaoh''s
    Curse, Triton''s Conch, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.64
      pick: 0.11
      fit: 0.15
    Berserker's Shield:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.33
    Devourer's Gauntlet:
      total: 0.51
      efficiency: 0.4
      win: 0.66
      pick: 0.42
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.82
      win: 0.59
      pick: 0.0
      fit: 0.11
  community_ordered:
  - Genji's Guard
  - Devourer's Gauntlet
  swaps:
  - added: Devourer's Gauntlet
    removed: Shield Splitter
    reason: community 66% win over 97 matches (vs 55% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-09-24'
  partial_windows:
    ob44: '2026-09-24'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of Transformation
    status: shown
    window: ob46
    window_rule: last closed
    window_start: '2026-10-20'
    window_end: '2026-11-03'
    matches: 50
    wins: 28
    win_share: 0.56
    aggregate:
      aspect_matches: 56
      aspect_win_rate: 0.536
      no_aspect_matches: 850
      no_aspect_win_rate: 0.534
    roles:
    - role: Solo
      matches: 41
      share: 0.82
    - role: Mid
      matches: 6
      share: 0.12
    - role: Support
      matches: 2
      share: 0.04
    - role: Jungle
      matches: 1
      share: 0.02
    base_role: Solo
    base_role_share: 0.82
    role_shift: null
    items:
    - name: Rod of Tahuti
      share: 0.32
    - name: Chronos' Pendant
      share: 0.3
    - name: Freya's Tears
      share: 0.28
    - name: Book of Thoth
      share: 0.24
    - name: brawlers-ruin
      share: 0.24
    - name: Devourer's Gauntlet
      share: 0.22
    - name: Spear of Desolation
      share: 0.22
    - name: Ancient Signet
      share: 0.18
    starters:
    - name: Archmage's Gem
      share: 0.32
    - name: Bluestone Brooch
      share: 0.32
    - name: Conduit Gem
      share: 0.12
    relics:
    - name: purification-beads
      share: 0.34
    - name: aegis-of-acceleration
      share: 0.3
    - name: phantom-shell
      share: 0.2
    matches_by_window:
      ob47: 26
      ob46: 50
      ob45: 73
      ob44: 84
    unmapped_slugs:
    - aegis-of-acceleration
    - agility-relic
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---
