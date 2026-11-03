---
type: smite-build
god: Ullr
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Tyrfing
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
    Toxic Blade:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.42
    Tyrfing:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Reaper:
      total: 0.61
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.62
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.49
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.58
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.6
    Heartseeker:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Rage
  - Jotunn's Revenge
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
    Rage:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.4
    Riptalon:
      total: 0.62
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.78
    Demon Blade:
      total: 0.51
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.66
    Deathbringer:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Ability / burst skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Reaper:
      total: 0.6
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Tekko-Kagi:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Titan's Bane:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.43
    Heartseeker:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - The Reaper
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.6
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.39
    The Reaper:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.74
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.83
    Pharaoh's Curse:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shogun's Ofuda:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tekko-Kagi
  - Riptalon
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Titan's Bane
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.65
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.85
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.53
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Riptalon:
      total: 0.67
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.88
    Titan's Bane:
      total: 0.54
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.63
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.81
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.33
    Tyrfing:
      total: 0.55
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Reaper:
      total: 0.57
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.58
    Riptalon:
      total: 0.65
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.84
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Chandra's Grace
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Pendulum Blade
  flex_slots:
  - Tyrfing
  - Pendulum Blade
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
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.55
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
    Chandra's Grace:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.45
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.47
    Pendulum Blade:
      total: 0.44
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Tyrfing
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.51
    Toxic Blade:
      total: 0.6
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.42
    Tyrfing:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Reaper:
      total: 0.61
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.63
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
---
