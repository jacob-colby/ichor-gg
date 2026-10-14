---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.43
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.5
    - name: Runeforged Hammer
      pick_rate: 0.08
      win_rate: 0.4
  - name: Sanguine Lash
    pick_rate: 0.3
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.35
    - name: Dagger of Frenzy
      pick_rate: 0.07
      win_rate: 0.53
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.41
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.55
    - name: Brawler’s Beat Stick
      pick_rate: 0.07
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.5
    - name: Brawler’s Beat Stick
      pick_rate: 0.06
      win_rate: 0.64
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.53
    - name: Sundering Echo
      pick_rate: 0.05
      win_rate: 0.73
  - name: Medal of Defense
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.43
  - name: Sundering Axe
    pick_rate: 0.14
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-10-14'
  god_win_rate: 0.49612403100775193
  god_matches_won: 128
  god_matches_played: 258
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-14'
  god_matches_analyzed: 8861
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Heartseeker
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Eye of the Storm,
    Shield Splitter, Heartseeker, Avenging Blade, Berserker''s Shield, Genji''s Guard,
    Hydra''s Lament, Breastplate of Valor, Titan''s Bane, The Crusher, Draconic Scale,
    Erosion, The Reaper, Eye of Providence, Runeforged Hammer, Shield of the Phoenix,
    Golden Blade, Daybreak Gavel, Midgardian Mail, Avatar''s Parashu, Stone of Binding,
    Leviathan''s Hide, Void Shield, Pendulum Blade, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Eye of the Storm:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.69
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Amanita Charm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament,
    Heartseeker, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Avenging Blade, Titan''s Bane, The Crusher, Shield of the Phoenix, Transcendence,
    Daybreak Gavel, The Reaper, Arondight, Draconic Scale, Runeforged Hammer, Screeching
    Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Pendulum
    Blade, Midgardian Mail, Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Eye of the Storm
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Eye of the Storm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix,
    The Reaper, Shield Splitter, Eye of the Storm, Berserker''s Shield, Draconic Scale,
    Erosion, Genji''s Guard, Eye of Providence, Breastplate of Valor, Yogi''s Necklace,
    Avenging Blade, Phoenix Feather, Heartseeker, Hydra''s Lament, Stone of Binding,
    Midgardian Mail, Titan''s Bane, Chandra''s Grace, The Crusher, Runeforged Hammer,
    Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.72
    Eye of the Storm:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Heartseeker, Amanita Charm, Titan''s
    Bane, The Crusher, Stone of Binding, The Reaper, Kinetic Cuirass, Void Shield,
    Screeching Gargoyle, Void Stone, Shield Splitter, Eye of the Storm, Avatar''s
    Parashu, Genji''s Guard, Berserker''s Shield, Breastplate of Valor, Pendulum Blade,
    Hydra''s Lament, Tekko-Kagi, Draconic Scale, Erosion, Daybreak Gavel, Eye of Providence,
    Shield of the Phoenix, Runeforged Hammer, Toxic Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.78
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.22
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.81
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Riptalon, Tyrfing, Silverbranch Bow, Toxic Blade, Kinetic Cuirass, Lernaean Bow,
    Genji''s Guard, Breastplate of Valor, Pharaoh''s Curse, Tekko-Kagi, The Reaper,
    Shogun''s Ofuda, Shield Splitter, Heartseeker, Eye of the Storm, Hydra''s Lament,
    Daybreak Gavel, Avenging Blade, Dominance, Erosion, Shield of the Phoenix, Eye
    of Providence, Qin''s Blade, Runeforged Hammer.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.27
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.6
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Hydra's Lament
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Berserker''s Shield, Arondight, Gladiator''s Shield,
    Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic Cloak, Chandra''s Grace,
    Heartseeker, Eye of the Storm, Daybreak Gavel, Draconic Scale, Erosion, Eye of
    Providence, Avenging Blade, Midgardian Mail, Stone of Binding, Titan''s Bane,
    The Crusher, Runeforged Hammer.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.46
      pick: 0.25
      fit: 0.52
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Eye of the Storm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Eye of the Storm, Shield Splitter, Heartseeker, Avenging Blade,
    Berserker''s Shield, Genji''s Guard, Hydra''s Lament, Breastplate of Valor, Titan''s
    Bane, The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Golden Blade, Daybreak Gavel, Midgardian Mail, Avatar''s Parashu,
    Stone of Binding, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Pendulum
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Eye of the Storm:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.57
      win: 0.4
      pick: 0.08
      fit: 0.59
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Runeforged Hammer
  starter: *id001
---
