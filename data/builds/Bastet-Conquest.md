---
type: smite-build
god: Bastet
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Watchful Pride
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.45
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.57
    win_rate: 0.45
    alternates:
    - name: Transcendence
      pick_rate: 0.11
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.55
  - name: Transcendence
    pick_rate: 0.24
    win_rate: 0.43
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.48
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.54
  - name: Pendulum Blade
    pick_rate: 0.17
    win_rate: 0.43
    alternates:
    - name: The Crusher
      pick_rate: 0.16
      win_rate: 0.48
    - name: Barbed Carver
      pick_rate: 0.14
      win_rate: 0.62
  - name: Heartseeker
    pick_rate: 0.34
    win_rate: 0.53
    alternates:
    - name: The Reaper
      pick_rate: 0.11
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.36
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Heartseeker
      pick_rate: 0.17
      win_rate: 0.35
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.53
  - name: Lucerne Hammer
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Titan's Bane
      pick_rate: 0.16
      win_rate: 0.63
    - name: Skeggox
      pick_rate: 0.09
      win_rate: 0.56
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.31
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.29
    win_rate: 0.38
  - name: Pendulum of The Ages
    pick_rate: 0.1
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/bastet/
  last_verified: '2026-08-14'
  god_win_rate: 0.46875
  god_matches_won: 90
  god_matches_played: 192
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Tekko-Kagi, Runeforged Hammer, Lernaean Bow, Damaru,
    Avatar''s Parashu, Golden Blade, Genji''s Guard, Avenging Blade, Shield Splitter,
    Arondight, Riptalon, Dominance, Eye of the Storm, Tyrfing, Silverbranch Bow, Breastplate
    of Valor, Berserker''s Shield, Deathbringer, Bloodforge, Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.45
      pick: 0.57
      fit: 1.0
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.91
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.48
      pick: 0.25
      fit: 1.0
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.53
      pick: 0.57
      fit: 1.0
    Titan's Bane:
      total: 0.54
      efficiency: 0.45
      win: 0.52
      pick: 0.28
      fit: 0.91
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Genji''s Guard, Breastplate of Valor, Riptalon, Runeforged
    Hammer, Silverbranch Bow, Tekko-Kagi, Freya''s Tears, Berserker''s Shield, Lernaean
    Bow, Damaru, Arondight, Shield of the Phoenix, Kinetic Cuirass, Golden Blade,
    Amanita Charm, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s Grace, Avatar''s
    Parashu, Eye of Providence, Avenging Blade, Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.45
      pick: 0.57
      fit: 0.78
    Hydra's Lament:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.56
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.48
      pick: 0.25
      fit: 0.66
    Heartseeker:
      total: 0.52
      efficiency: 0.45
      win: 0.53
      pick: 0.57
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Shifter''s Shield, Genji''s Guard, Oni Hunter''s Garb, Runeforged Hammer,
    Eye of the Storm, Riptalon, Chandra''s Grace, Shield Splitter, Erosion, Phoenix
    Feather, Freya''s Tears, Breastplate of Valor, Eye of Providence, Spectral Armor,
    Pharaoh''s Curse, Draconic Scale, Hydra''s Lament, Golden Blade, Leviathan''s
    Hide, Avenging Blade, Midgardian Mail, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.45
      pick: 0.57
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.56
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.7
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.48
      pick: 0.25
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Tekko-Kagi, Riptalon, Silverbranch Bow, Avenging Blade, Avatar''s
    Parashu, Hydra''s Lament, Genji''s Guard, Runeforged Hammer, Lernaean Bow, Damaru,
    Toxic Blade, Screeching Gargoyle, Breastplate of Valor, Berserker''s Shield, Golden
    Blade, Shield Splitter, Stone of Binding, Dominance, Eye of the Storm, Oath-Sworn
    Spear, Tyrfing, Kinetic Cuirass, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.45
      pick: 0.57
      fit: 1.0
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.94
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.48
      pick: 0.25
      fit: 1.0
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.53
      pick: 0.57
      fit: 1.0
    Titan's Bane:
      total: 0.55
      efficiency: 0.45
      win: 0.52
      pick: 0.28
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Silverbranch Bow, Golden Blade, Berserker''s Shield, Tyrfing,
    Lernaean Bow, Genji''s Guard, Tekko-Kagi, Toxic Blade, Dominance, Hydra''s Lament,
    Pharaoh''s Curse, Breastplate of Valor, Runeforged Hammer, Shogun''s Ofuda, Damaru,
    Eros'' Bow, Qin''s Blade, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb,
    Eye of Providence, Freya''s Tears, Dagger of Frenzy.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.45
      pick: 0.57
      fit: 0.37
    The Reaper:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.44
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.48
      pick: 0.25
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  flex_slots:
  - The Crusher
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Hydra''s Lament, Breastplate
    of Valor, Freya''s Tears, Shield of the Phoenix, Arondight, Screeching Gargoyle,
    Chandra''s Grace, Berserker''s Shield, Gladiator''s Shield, Runeforged Hammer,
    Riptalon, Lernaean Bow, Damaru, Prophetic Cloak, Kinetic Cuirass, Amanita Charm,
    Silverbranch Bow, Oni Hunter''s Garb, Eye of Providence, Regrowth Striders, Golden
    Blade, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.45
      pick: 0.57
      fit: 0.85
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.75
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.48
      pick: 0.25
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Hydra''s Lament, Tekko-Kagi, Runeforged Hammer, Lernaean
    Bow, Damaru, Avatar''s Parashu, Golden Blade, Genji''s Guard, Avenging Blade,
    Shield Splitter, Arondight, Riptalon, Dominance, Eye of the Storm, Tyrfing, Silverbranch
    Bow, Breastplate of Valor, Berserker''s Shield, Deathbringer, Bloodforge, Musashi''s
    Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.45
      pick: 0.57
      fit: 1.0
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.91
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.48
      pick: 0.25
      fit: 1.0
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.53
      pick: 0.57
      fit: 1.0
    Titan's Bane:
      total: 0.54
      efficiency: 0.45
      win: 0.52
      pick: 0.28
      fit: 0.91
  starter: *id001
---
