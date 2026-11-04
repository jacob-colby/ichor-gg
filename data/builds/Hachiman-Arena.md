---
type: smite-build
god: Hachiman
mode: Arena
builds:
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Tyrfing
  - Golden Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Toxic Blade:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Tyrfing:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Reaper:
      total: 0.65
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.74
    Riptalon:
      total: 0.67
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
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
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.46
    Transcendence:
      total: 0.39
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.25
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Toxic Blade
  - Rage
  - Riptalon
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Rage
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Crit / auto-attack skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.62
    Toxic Blade:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Rage:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    Riptalon:
      total: 0.65
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.85
    Demon Blade:
      total: 0.55
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.73
    Deathbringer:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.5
    Toxic Blade:
      total: 0.54
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.47
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Reaper:
      total: 0.61
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.66
    Titan's Bane:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Toxic Blade:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - The Reaper
  - Tekko-Kagi
  - Silverbranch Bow
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Silverbranch Bow
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
      total: 0.64
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.83
    The Reaper:
      total: 0.71
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.85
    Tekko-Kagi:
      total: 0.58
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.61
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Titan's Bane:
      total: 0.58
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.61
    Heartseeker:
      total: 0.57
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Golden Blade
  - Lernaean Bow
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Arena — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.68
    Lernaean Bow:
      total: 0.56
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.6
    Toxic Blade:
      total: 0.62
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
    Tyrfing:
      total: 0.59
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Reaper:
      total: 0.59
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.62
    Riptalon:
      total: 0.69
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Lernaean Bow
  - Toxic Blade
  - Chandra's Grace
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  flex_slots:
  - Lernaean Bow
  - Tyrfing
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Arena — math + mode profile (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.46
    Toxic Blade:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
    Chandra's Grace:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Toxic Blade
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Tyrfing
  - Golden Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Arena — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.59
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.66
    Toxic Blade:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
    Tyrfing:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Reaper:
      total: 0.65
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.74
    Riptalon:
      total: 0.67
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
---
