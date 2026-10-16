---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.7
  aspect_win_rate: 0.57
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.44
    win_rate: 0.62
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.25
      win_rate: 0.62
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.47
  - name: Jotunn's Revenge
    pick_rate: 0.28
    win_rate: 0.59
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.51
    - name: Sanguine Lash
      pick_rate: 0.15
      win_rate: 0.63
  - name: Barbed Carver
    pick_rate: 0.27
    win_rate: 0.6
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.62
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.52
  - name: The Reaper
    pick_rate: 0.2
    win_rate: 0.54
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.49
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.48
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.57
  - name: Tekko-Kagi
    pick_rate: 0.1
    win_rate: 0.62
    alternates:
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.33
    - name: Magi's Cloak
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.33
    win_rate: 0.69
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.59
  - name: Leather Cowl
    pick_rate: 0.15
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-10-16'
  god_win_rate: 0.5804988662131519
  god_matches_won: 256
  god_matches_played: 441
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-16'
  god_matches_analyzed: 10934
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Runeforged Hammer
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Runeforged Hammer
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged Hammer,
    Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic Blade, Shifter''s
    Shield, Pharaoh''s Curse, Avenging Blade, Titan''s Bane, Shogun''s Ofuda, The
    Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence,
    Shield of the Phoenix, Hydra''s Lament.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.09
      fit: 0.4
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.62
      pick: 0.31
      fit: 0.51
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Berserker''s
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Golden Blade, Freya''s Tears, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter,
    Eye of the Storm, Titan''s Bane, Avenging Blade, Silverbranch Bow, Shifter''s
    Shield, Dominance, Daybreak Gavel, Shield of the Phoenix, Pharaoh''s Curse, The
    Crusher, Toxic Blade, Transcendence, Deathbringer, Eye of Providence, Shogun''s
    Ofuda, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.09
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.41
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.2
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.62
      pick: 0.31
      fit: 0.39
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.21
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Tekko-Kagi
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Golden Blade, Runeforged Hammer, Riptalon, Freya''s Tears, Shield Splitter, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Yogi''s Necklace, Eye of the Storm,
    Lernaean Bow, Tyrfing, Pharaoh''s Curse, Phoenix Feather, Erosion, Shogun''s Ofuda,
    Toxic Blade, Eye of Providence, Avenging Blade, Silverbranch Bow, Draconic Scale,
    Hydra''s Lament.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.09
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.32
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.62
      pick: 0.31
      fit: 0.45
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Berserker''s Shield, Amanita Charm, Stone of Binding,
    Silverbranch Bow, Golden Blade, Toxic Blade, Runeforged Hammer, Titan''s Bane,
    Screeching Gargoyle, Void Shield, Kinetic Cuirass, Void Stone, The Crusher, Genji''s
    Guard, Breastplate of Valor, Lernaean Bow, Tyrfing, Freya''s Tears, Shield Splitter,
    Riptalon, Eye of the Storm, Shifter''s Shield, Pharaoh''s Curse, Avatar''s Parashu,
    Hydra''s Lament.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.54
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.48
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.09
      fit: 0.33
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.62
      pick: 0.31
      fit: 0.6
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Riptalon
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Golden Blade, Riptalon, Tyrfing,
    Silverbranch Bow, Kinetic Cuirass, Runeforged Hammer, Toxic Blade, Genji''s Guard,
    Lernaean Bow, Breastplate of Valor, Freya''s Tears, Pharaoh''s Curse, Shogun''s
    Ofuda, Shifter''s Shield, Shield Splitter, Daybreak Gavel, Eye of the Storm, Avenging
    Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Stone of
    Binding, Hydra''s Lament.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.24
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.09
      fit: 0.38
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.62
      pick: 0.31
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  - Tekko-Kagi
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Breastplate of Valor
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Berserker''s Shield, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Silverbranch Bow,
    Shifter''s Shield, Lernaean Bow, Arondight, Tyrfing, Pharaoh''s Curse, Shield
    Splitter, Daybreak Gavel, Toxic Blade, Eye of Erebus, Shogun''s Ofuda, Eye of
    the Storm, Gladiator''s Shield, Hydra''s Lament, Avenging Blade, Erosion, Eye
    of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.09
      fit: 0.3
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.33
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.24
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Tyrfing, Lernaean Bow, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Eye of the Storm, Silverbranch Bow, Toxic
    Blade, Shifter''s Shield, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s
    Ofuda, Titan''s Bane, The Crusher, Daybreak Gavel, Deathbringer, Dominance, Erosion,
    Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.09
      fit: 0.4
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.32
  community_ordered:
  - Jotunn's Revenge
  - Berserker's Shield
  starter: *id001
---
