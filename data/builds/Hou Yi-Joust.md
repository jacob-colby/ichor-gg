---
type: smite-build
god: Hou Yi
mode: Joust
builds:
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Death Metal
  - Riptalon
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Death Metal
  - Demon Blade
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Top weighted-score core (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.8
    Demon Blade:
      total: 0.56
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.69
      efficiency: 0.57
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
  - Bancroft's Talon
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Bancroft's Talon
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: mana-stack (efficiency + fit). Joust — math + mode profile (no meta win/pick
    data).
  slot_scores:
    Toxic Blade:
      total: 0.54
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Bancroft's Talon:
      total: 0.53
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Bragi's Harp:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Death Metal
  - Demon Blade
  - Deathbringer
  - Soul Gem
  flex_slots:
  - Tyrfing
  - Deathbringer
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Crit / auto-attack skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.64
    Death Metal:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
    Demon Blade:
      total: 0.57
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.75
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.49
    Soul Gem:
      total: 0.68
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Amanita Charm
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Shogun's Ofuda
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: Lifesteal bruiser skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.72
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.76
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
    Pharaoh's Curse:
      total: 0.57
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shogun's Ofuda:
      total: 0.56
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.67
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Full-penetration anti-tank skew (efficiency + fit). Joust — math + mode
    profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.67
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.9
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.47
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Death Metal
  - Qin's Blade
  - Riptalon
  - Soul Gem
  flex_slots:
  - Death Metal
  - Qin's Blade
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Basic-attack DPS skew (efficiency + fit). Joust — math + mode profile
    (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.61
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.41
    Qin's Blade:
      total: 0.5
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.63
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.66
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.5
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.43
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Umbral Link — physical protection
    swap_item: Umbral Link
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Off-type Intelligence build — this kit scales on it (efficiency + fit).
    Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.56
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.78
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Bragi's Harp
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.58
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Bragi's Harp:
      total: 0.55
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.33
    Soul Gem:
      total: 0.77
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Death Metal
  - Riptalon
  - Demon Blade
  - Soul Gem
  flex_slots:
  - Death Metal
  - Demon Blade
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's own answer — no meta signal (efficiency + fit). Joust — math
    + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.8
    Demon Blade:
      total: 0.56
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Death Metal
  - Silverbranch Bow
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: The model's core, corrected where the community is clearly right (efficiency
    + fit). Joust — math + mode profile (no meta win/pick data).
  slot_scores:
    Toxic Blade:
      total: 0.59
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.74
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.8
    Silverbranch Bow:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Soul Gem:
      total: 0.69
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
  swaps:
  - added: Silverbranch Bow
    removed: Demon Blade
    reason: Conquest community 71% win over 46 matches (vs 53% on this god), taking
      the model's weakest slot from Demon Blade
  borrowed_from: Conquest
  starter: *id001
---
