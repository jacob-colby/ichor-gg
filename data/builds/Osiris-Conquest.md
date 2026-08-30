---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.53
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.45
    win_rate: 0.52
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.42
    - name: Golden Blade
      pick_rate: 0.07
      win_rate: 0.3
  - name: Prophetic Cloak
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.39
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.56
  - name: Gladiator's Shield
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.18
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.63
  - name: Ethereal Staff
    pick_rate: 0.09
    win_rate: 0.73
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.2
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.64
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.56
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.75
  - name: Draconic Scale
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.4
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.75
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.23
    win_rate: 0.55
  - name: Warrior's Axe
    pick_rate: 0.2
    win_rate: 0.41
  - name: Death's Embrace
    pick_rate: 0.18
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-30'
  god_win_rate: 0.5109489051094891
  god_matches_won: 70
  god_matches_played: 137
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-30'
  god_matches_analyzed: 5563
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Runeforged Hammer
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Shogun''s Ofuda,
    Runeforged Hammer, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s Lament,
    Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic Blade, Erosion, Silverbranch
    Bow, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Midgardian Mail,
    Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.8
      pick: 0.13
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.23
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.35
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.09
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Shield of the Phoenix
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix,
    Shogun''s Ofuda, Runeforged Hammer, Shield Splitter, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean
    Bow, Tyrfing, Riptalon, Erosion, Phoenix Feather, Eye of Providence, Avenging
    Blade, Hydra''s Lament, Chandra''s Grace, Stone of Binding, Daybreak Gavel, Midgardian
    Mail, Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.8
      pick: 0.13
      fit: 0.54
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.3
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.74
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.09
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Jotunn''s Revenge, Avenging Blade, Amanita Charm,
    Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Runeforged Hammer,
    Screeching Gargoyle, Void Shield, Toxic Blade, Titan''s Bane, Void Stone, The
    Crusher, Genji''s Guard, Breastplate of Valor, Lernaean Bow, The Reaper, Tyrfing,
    Shield Splitter, Hydra''s Lament, Riptalon, Eye of the Storm, Pharaoh''s Curse,
    Avatar''s Parashu, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.8
      pick: 0.13
      fit: 0.36
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.17
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Freya's Tears
  - Riptalon
  - Shogun's Ofuda
  flex_slots:
  - Tyrfing
  - Riptalon
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
    this god: Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Shogun''s Ofuda,
    Tyrfing, Riptalon, Runeforged Hammer, Lernaean Bow, Genji''s Guard, Silverbranch
    Bow, Breastplate of Valor, Pharaoh''s Curse, Toxic Blade, Shield Splitter, Eye
    of the Storm, Hydra''s Lament, Tekko-Kagi, The Reaper, Daybreak Gavel, Avenging
    Blade, Dominance, Erosion, Shield of the Phoenix, Eye of Providence, Heartseeker,
    Vital Amplifier, Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.18
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.8
      pick: 0.13
      fit: 0.36
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.17
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.48
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.5
      win: 0.63
      pick: 0.09
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Jotunn''s Revenge,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of
    the Phoenix, Shogun''s Ofuda, Screeching Gargoyle, Runeforged Hammer, Arondight,
    Lernaean Bow, Pharaoh''s Curse, Tyrfing, Shield Splitter, Daybreak Gavel, Eye
    of Erebus, Eye of the Storm, Chandra''s Grace, Silverbranch Bow, Erosion, Avenging
    Blade, Eye of Providence, Stone of Binding, Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.8
      pick: 0.13
      fit: 0.36
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.26
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Lernaean Bow, Tyrfing, Shield Splitter, Eye of the Storm,
    Genji''s Guard, Breastplate of Valor, Pharaoh''s Curse, Avenging Blade, Hydra''s
    Lament, Shogun''s Ofuda, Tekko-Kagi, Heartseeker, Dominance, Deathbringer, Toxic
    Blade, Erosion, Silverbranch Bow, Daybreak Gavel, Eye of Providence, Shield of
    the Phoenix, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.42
      efficiency: 0.52
      win: 0.3
      pick: 0.07
      fit: 0.64
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.39
      pick: 0.18
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.8
      pick: 0.13
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.35
  starter: *id001
---
