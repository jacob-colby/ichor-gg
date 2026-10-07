---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.29
    win_rate: 0.71
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.25
      win_rate: 0.33
    - name: Avenging Blade
      pick_rate: 0.17
      win_rate: 0.25
  - name: Sanguine Lash
    pick_rate: 0.25
    win_rate: 0.83
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.33
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.0
  - name: Brawler’s Beat Stick
    pick_rate: 0.17
    win_rate: 0.75
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.0
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.0
  - name: Contagion
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 1.0
  - name: Medal of Defense
    pick_rate: 0.22
    win_rate: 0.0
    alternates:
    - name: Contagion
      pick_rate: 0.11
      win_rate: 1.0
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 1.0
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.5
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-10-07'
  god_win_rate: 0.4166666666666667
  god_matches_won: 10
  god_matches_played: 24
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  flex_slots:
  - Brawler’s Beat Stick
  - Runeforged Hammer
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Kinetic Cuirass,
    Eye of the Storm, Shield Splitter, Heartseeker, Breastplate of Valor, Genji''s
    Guard, Hydra''s Lament, Titan''s Bane, The Crusher, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Golden Blade, Daybreak Gavel, Midgardian
    Mail, Avatar''s Parashu, Stone of Binding, Hide of the Nemean Lion, Leviathan''s
    Hide, Void Shield, Pendulum Blade, Berserker''s Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.54
      efficiency: 0.42
      win: 0.75
      pick: 0.26
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.26
      fit: 0.3
    The Reaper:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.49
    Dwarven Plate:
      total: 0.64
      efficiency: 0.4
      win: 1.0
      pick: 0.34
      fit: 0.26
  community_ordered:
  - Brawler’s Beat Stick
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Genji''s Guard, Hydra''s Lament,
    Runeforged Hammer, Heartseeker, Kinetic Cuirass, Shield Splitter, Eye of the Storm,
    Titan''s Bane, The Crusher, Shield of the Phoenix, Transcendence, Daybreak Gavel,
    Arondight, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian Mail, Golden Blade,
    Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.14
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.72
      efficiency: 0.61
      win: 1.0
      pick: 0.26
      fit: 0.25
    The Reaper:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.34
    Dwarven Plate:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.34
      fit: 0.15
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Sanguine Lash
  - Dwarven Plate
  flex_slots:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Breastplate of Valor, Erosion,
    Genji''s Guard, Eye of Providence, Yogi''s Necklace, Draconic Scale, Phoenix Feather,
    Heartseeker, Hydra''s Lament, Stone of Binding, Midgardian Mail, Titan''s Bane,
    Chandra''s Grace, The Crusher, Daybreak Gavel, Hide of the Nemean Lion, Magi''s
    Cloak, Leviathan''s Hide, Berserker''s Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.55
      efficiency: 0.42
      win: 0.75
      pick: 0.26
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.26
      fit: 0.38
    The Reaper:
      total: 0.74
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.71
    Sanguine Lash:
      total: 0.59
      efficiency: 0.36
      win: 0.83
      pick: 0.34
      fit: 0.51
    Dwarven Plate:
      total: 0.66
      efficiency: 0.4
      win: 1.0
      pick: 0.34
      fit: 0.34
  community_ordered:
  - Brawler’s Beat Stick
  - Freya's Tears
  - The Reaper
  - Sanguine Lash
  - Dwarven Plate
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  - Heartseeker
  flex_slots:
  - Brawler’s Beat Stick
  - Heartseeker
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Heartseeker, Amanita Charm, Titan''s Bane, The
    Crusher, Runeforged Hammer, Stone of Binding, Kinetic Cuirass, Void Shield, Screeching
    Gargoyle, Void Stone, Breastplate of Valor, Shield Splitter, Eye of the Storm,
    Avatar''s Parashu, Genji''s Guard, Pendulum Blade, Hydra''s Lament, Tekko-Kagi,
    Erosion, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Draconic Scale,
    Toxic Blade, Berserker''s Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.53
      efficiency: 0.42
      win: 0.75
      pick: 0.26
      fit: 0.2
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.71
      efficiency: 0.61
      win: 1.0
      pick: 0.26
      fit: 0.23
    The Reaper:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.61
    Dwarven Plate:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.34
      fit: 0.2
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Brawler’s Beat Stick
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Tyrfing
  - Freya's Tears
  - The Reaper
  - Riptalon
  - Dwarven Plate
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Golden Blade, Amanita Charm, Riptalon, Tyrfing, Silverbranch
    Bow, Toxic Blade, Kinetic Cuirass, Breastplate of Valor, Runeforged Hammer, Lernaean
    Bow, Genji''s Guard, Pharaoh''s Curse, Tekko-Kagi, Shogun''s Ofuda, Shield Splitter,
    Heartseeker, Eye of the Storm, Hydra''s Lament, Daybreak Gavel, Dominance, Erosion,
    Shield of the Phoenix, Eye of Providence, Qin''s Blade, Berserker''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.62
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.7
      efficiency: 0.61
      win: 1.0
      pick: 0.26
      fit: 0.18
    The Reaper:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.15
      fit: 0.32
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.58
    Dwarven Plate:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.34
      fit: 0.15
  community_ordered:
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
  flex_slots:
  - Breastplate of Valor
  - Brawler’s Beat Stick
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Sanguine Lash — magical protection
    swap_item: Sanguine Lash
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Genji''s Guard, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Arondight, Gladiator''s
    Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic Cloak, Chandra''s
    Grace, Heartseeker, Eye of the Storm, Daybreak Gavel, Erosion, Eye of Providence,
    Draconic Scale, Midgardian Mail, Stone of Binding, Titan''s Bane, The Crusher,
    Berserker''s Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.42
      win: 0.75
      pick: 0.26
      fit: 0.17
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.14
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.26
      fit: 0.52
    The Reaper:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.24
    Dwarven Plate:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.34
      fit: 0.17
  community_ordered:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Freya's Tears
  - The Reaper
  - Dwarven Plate
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
    Kinetic Cuirass, Eye of the Storm, Shield Splitter, Heartseeker, Berserker''s
    Shield, Genji''s Guard, Hydra''s Lament, Breastplate of Valor, Titan''s Bane,
    The Crusher, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Golden Blade, Daybreak Gavel, Midgardian Mail, Avatar''s Parashu, Stone of Binding,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Pendulum Blade.'
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
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
---
