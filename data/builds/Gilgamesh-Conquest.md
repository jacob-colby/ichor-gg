---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.44
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.3
    win_rate: 0.54
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.23
      win_rate: 0.48
    - name: Golden Blade
      pick_rate: 0.08
      win_rate: 0.6
  - name: Berserker's Shield
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.57
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.53
  - name: Kinetic Cuirass
    pick_rate: 0.11
    win_rate: 0.48
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.14
      win_rate: 0.58
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.57
  - name: Heartseeker
    pick_rate: 0.08
    win_rate: 0.46
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.63
    - name: The Reaper
      pick_rate: 0.06
      win_rate: 0.66
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.61
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.61
  - name: The Crusher
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.55
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.61
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.35
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.41
  - name: Bumba's Hammer
    pick_rate: 0.09
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-08-22'
  god_win_rate: 0.5496402877697841
  god_matches_won: 382
  god_matches_played: 695
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Runeforged Hammer
  - The Reaper
  flex_slots:
  - Runeforged Hammer
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, Runeforged Hammer, Tyrfing, Lernaean Bow,
    Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor, Freya''s Tears,
    Eye of the Storm, Silverbranch Bow, Toxic Blade, Hydra''s Lament, Pharaoh''s Curse,
    Avenging Blade, Shogun''s Ofuda, Titan''s Bane, Daybreak Gavel, Deathbringer,
    Dominance, Erosion, Eye of Providence, Shield of the Phoenix, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.08
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.25
      fit: 0.4
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.23
      fit: 0.37
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.53
      efficiency: 0.5
      win: 0.66
      pick: 0.1
      fit: 0.34
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Reaper
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Golden
    Blade, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Hydra''s Lament, Freya''s Tears, Lernaean Bow, Tyrfing, Shield Splitter, Tekko-Kagi,
    Eye of the Storm, Avenging Blade, Silverbranch Bow, Dominance, Daybreak Gavel,
    Shield of the Phoenix, Titan''s Bane, Pharaoh''s Curse, Toxic Blade, Deathbringer,
    Eye of Providence, Transcendence, Shogun''s Ofuda, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.08
      fit: 0.43
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.25
      fit: 0.27
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.23
      fit: 0.41
    The Reaper:
      total: 0.52
      efficiency: 0.5
      win: 0.66
      pick: 0.1
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Golden Blade, Shield of the Phoenix, Runeforged
    Hammer, Riptalon, Freya''s Tears, Shield Splitter, Genji''s Guard, Breastplate
    of Valor, Yogi''s Necklace, Eye of the Storm, Lernaean Bow, Tyrfing, Pharaoh''s
    Curse, Phoenix Feather, Erosion, Shogun''s Ofuda, Tekko-Kagi, Toxic Blade, Eye
    of Providence, Avenging Blade, Silverbranch Bow, Hydra''s Lament, Draconic Scale,
    Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.08
      fit: 0.56
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.25
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.23
      fit: 0.32
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.66
      pick: 0.1
      fit: 0.6
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.54
      pick: 0.3
      fit: 0.4
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  flex_slots:
  - Avenging Blade
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Golden Blade, Avenging Blade, Amanita Charm, Tekko-Kagi,
    Stone of Binding, Silverbranch Bow, Toxic Blade, Runeforged Hammer, Screeching
    Gargoyle, Void Shield, Titan''s Bane, Void Stone, Genji''s Guard, Breastplate
    of Valor, Lernaean Bow, Tyrfing, Freya''s Tears, Shield Splitter, Riptalon, Hydra''s
    Lament, Eye of the Storm, Pharaoh''s Curse, Heartseeker, Avatar''s Parashu.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.08
      fit: 0.5
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.25
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.23
      fit: 0.48
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.66
      pick: 0.1
      fit: 0.45
    The Crusher:
      total: 0.51
      efficiency: 0.47
      win: 0.57
      pick: 0.18
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, The Reaper, Amanita Charm, Riptalon, Tyrfing, Silverbranch
    Bow, Runeforged Hammer, Toxic Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Freya''s Tears, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda, Shield
    Splitter, Hydra''s Lament, Daybreak Gavel, Eye of the Storm, Avenging Blade, Dominance,
    Erosion, Shield of the Phoenix, Eye of Providence, Stone of Binding, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.08
      fit: 0.56
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.25
      fit: 0.38
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.48
      pick: 0.23
      fit: 0.24
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.55
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.66
      pick: 0.1
      fit: 0.28
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Golden Blade, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Screeching Gargoyle, Runeforged Hammer, Silverbranch Bow, Lernaean Bow, Arondight,
    Tyrfing, Pharaoh''s Curse, Shield Splitter, Daybreak Gavel, Toxic Blade, Eye of
    Erebus, Shogun''s Ofuda, Tekko-Kagi, Eye of the Storm, Gladiator''s Shield, Avenging
    Blade, Erosion, Eye of Providence, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.08
      fit: 0.38
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.25
      fit: 0.3
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.23
      fit: 0.45
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
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
    Underrated for this god: Amanita Charm, Golden Blade, Runeforged Hammer, Tyrfing,
    Lernaean Bow, Shield Splitter, Tekko-Kagi, Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Eye of the Storm, Heartseeker, Silverbranch Bow, Toxic Blade,
    Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Shogun''s Ofuda, Titan''s Bane,
    Daybreak Gavel, Deathbringer, Dominance, Erosion, Eye of Providence, Shield of
    the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.08
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.25
      fit: 0.4
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.23
      fit: 0.37
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.48
      pick: 0.17
      fit: 0.42
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.32
  starter: *id001
---
