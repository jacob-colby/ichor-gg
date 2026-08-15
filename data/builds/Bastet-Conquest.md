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
  - name: Pendulum of the Ages
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
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Hydra''s Lament, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow,
    Avatar''s Parashu, Golden Blade, Avenging Blade, Arondight, Shield Splitter, Genji''s
    Guard, Eye of the Storm, Tyrfing, Riptalon, Dominance, Silverbranch Bow, Breastplate
    of Valor, Deathbringer, Berserker''s Shield, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.45
      pick: 0.57
      fit: 1.0
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.43
      pick: 0.33
      fit: 0.52
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.91
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.48
      pick: 0.25
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.41
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
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Damaru, Lernaean
    Bow, Arondight, Oni Hunter''s Garb, Berserker''s Shield, Golden Blade, Freya''s
    Tears, Tekko-Kagi, Avenging Blade, Dominance, Kinetic Cuirass, Shield Splitter,
    Amanita Charm, Shield of the Phoenix, Eye of the Storm, Tyrfing, Eye of Providence,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.45
      pick: 0.57
      fit: 0.71
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.47
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.48
      pick: 0.25
      fit: 0.57
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.53
      pick: 0.57
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Freya''s Tears, Tekko-Kagi, Riptalon, Arondight, Damaru, Silverbranch Bow, Shield
    of the Phoenix, Berserker''s Shield, Lernaean Bow, Kinetic Cuirass, Amanita Charm,
    Screeching Gargoyle, Golden Blade, Chandra''s Grace, Eye of Providence, Avenging
    Blade, Oni Hunter''s Garb, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.45
      pick: 0.57
      fit: 0.78
    Transcendence:
      total: 0.43
      efficiency: 0.52
      win: 0.43
      pick: 0.33
      fit: 0.22
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.18
      fit: 0.56
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.48
      pick: 0.25
      fit: 0.66
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.53
      pick: 0.57
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Shifter''s Shield,
    Berserker''s Shield, Runeforged Hammer, Genji''s Guard, Oni Hunter''s Garb, Eye
    of the Storm, Chandra''s Grace, Erosion, Shield Splitter, Phoenix Feather, Freya''s
    Tears, Eye of Providence, Spectral Armor, Draconic Scale, Riptalon, Breastplate
    of Valor, Golden Blade, Pharaoh''s Curse, Hydra''s Lament, Leviathan''s Hide,
    Avenging Blade, Midgardian Mail, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
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
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.1
      fit: 0.56
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.48
      pick: 0.25
      fit: 0.5
    Amanita Charm:
      total: 0.57
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
    for this god: Tekko-Kagi, Riptalon, Avenging Blade, Silverbranch Bow, Avatar''s
    Parashu, Hydra''s Lament, Runeforged Hammer, Genji''s Guard, Damaru, Toxic Blade,
    Screeching Gargoyle, Lernaean Bow, Golden Blade, Breastplate of Valor, Berserker''s
    Shield, Shield Splitter, Stone of Binding, Eye of the Storm, Tyrfing, Oath-Sworn
    Spear, Arondight, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
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
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.48
      pick: 0.25
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.41
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
  - Silverbranch Bow
  - Jotunn's Revenge
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
    this god: Riptalon, Golden Blade, Silverbranch Bow, Tyrfing, Berserker''s Shield,
    Lernaean Bow, Toxic Blade, Tekko-Kagi, Genji''s Guard, Hydra''s Lament, Pharaoh''s
    Curse, Dominance, Runeforged Hammer, Breastplate of Valor, Damaru, Shogun''s Ofuda,
    Kinetic Cuirass, Amanita Charm, Qin''s Blade, Eye of Providence, Oni Hunter''s
    Garb, Eros'' Bow, Freya''s Tears, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
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
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.52
      efficiency: 0.64
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
    Chandra''s Grace, Gladiator''s Shield, Runeforged Hammer, Berserker''s Shield,
    Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita Charm, Riptalon, Eye of Providence,
    Oni Hunter''s Garb, Regrowth Striders, Lernaean Bow, Silverbranch Bow, Golden
    Blade, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.45
      pick: 0.57
      fit: 0.85
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
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
      efficiency: 0.64
      win: 0.48
      pick: 0.25
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    Underrated for this god: Hydra''s Lament, Tekko-Kagi, Runeforged Hammer, Damaru,
    Lernaean Bow, Avatar''s Parashu, Golden Blade, Avenging Blade, Arondight, Shield
    Splitter, Genji''s Guard, Eye of the Storm, Tyrfing, Riptalon, Dominance, Silverbranch
    Bow, Breastplate of Valor, Deathbringer, Berserker''s Shield, Musashi''s Dual
    Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.45
      pick: 0.57
      fit: 1.0
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.43
      pick: 0.33
      fit: 0.52
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
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
      efficiency: 0.64
      win: 0.48
      pick: 0.25
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.41
      win: 0.53
      pick: 0.57
      fit: 1.0
  starter: *id001
---
