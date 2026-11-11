---
type: smite-build
god: Xbalanque
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Demon Blade
  flex_slots:
  - Lernaean Bow
  - Qin's Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.64
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
    Lernaean Bow:
      total: 0.61
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.68
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.83
    Qin's Blade:
      total: 0.56
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.72
    Riptalon:
      total: 0.63
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.9
    Demon Blade:
      total: 0.62
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
    pick_rate: 0.8
    win_rate: 0.58
    matches: 362
    basis: community
    borrowed_from: Conquest
  relic: &id002
    name: Purification Beads
    pick_rate: 0.57
    win_rate: 0.55
    matches: 258
    basis: community
    borrowed_from: Conquest
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - The Reaper
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: mana-stack (efficiency + fit). Arena — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.37
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Reaper:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.6
    Heartseeker:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
  relic: *id002
- source: suggested
  archetype: crit
  slot_order:
  - Golden Blade
  - Rage
  - Tyrfing
  - Riptalon
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Rage
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rage:
      total: 0.52
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.57
    Tyrfing:
      total: 0.66
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.61
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.86
    Demon Blade:
      total: 0.62
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
  relic: *id002
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Magi's Cloak — physical protection
    swap_item: Magi's Cloak
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.69
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.58
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.69
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
  relic: *id002
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  - Heartseeker
  flex_slots:
  - Tyrfing
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Arena — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.67
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.9
    Tyrfing:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.59
    Riptalon:
      total: 0.72
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.69
    Heartseeker:
      total: 0.56
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
  relic: *id002
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Demon Blade
  flex_slots:
  - Qin's Blade
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Lernaean Bow:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Tyrfing:
      total: 0.64
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.75
    Qin's Blade:
      total: 0.54
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.69
    Riptalon:
      total: 0.6
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.84
    Demon Blade:
      total: 0.53
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
  relic: *id002
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Chandra's Grace
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  flex_slots:
  - Lernaean Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Talisman of Purification — CC-immunity / cleanse
    swap_item: Talisman of Purification
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.52
    Lernaean Bow:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Chandra's Grace:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
  relic: *id002
- source: suggested
  archetype: intelligence
  slot_order:
  - Toxic Blade
  - Death Metal
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Toxic Blade
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Off-type Intelligence build — this kit scales on it (efficiency + fit).
    Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.5
    Bragi's Harp:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.73
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
  relic: *id002
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Death Metal
  - Bragi's Harp
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sphere of Negation — magical protection
    swap_item: Sphere of Negation
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.57
    Bragi's Harp:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.82
      win: 0.5
      pick: 0.0
      fit: 0.34
    Soul Gem:
      total: 0.65
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.77
  starter: *id001
  relic: *id002
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Demon Blade
  flex_slots:
  - Lernaean Bow
  - Qin's Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.64
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
    Lernaean Bow:
      total: 0.61
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.68
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.83
    Qin's Blade:
      total: 0.56
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.72
    Riptalon:
      total: 0.63
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.9
    Demon Blade:
      total: 0.62
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
  relic: *id002
---
