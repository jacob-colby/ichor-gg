---
type: smite-build
god: Loki
mode: Conquest
builds:
- source: community
  aspect: Aspect of Agony
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.51
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.5
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.21
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.5
  - name: Hydra's Lament
    pick_rate: 0.26
    win_rate: 0.46
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.59
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.63
  - name: The Crusher
    pick_rate: 0.11
    win_rate: 0.61
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.64
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.45
  - name: Heartseeker
    pick_rate: 0.3
    win_rate: 0.59
    alternates:
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.48
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.63
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.56
    - name: The Reaper
      pick_rate: 0.05
      win_rate: 0.58
  - name: Skeggox
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.08
      win_rate: 0.62
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.82
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.38
    win_rate: 0.59
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.46
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/loki/
  last_verified: '2026-08-14'
  god_win_rate: 0.5353535353535354
  god_matches_won: 159
  god_matches_played: 297
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Pendulum Blade, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean
    Bow, Avatar''s Parashu, Golden Blade, Transcendence, Avenging Blade, Arondight,
    Shield Splitter, Genji''s Guard, Eye of the Storm, Tyrfing, Riptalon, Dominance,
    Silverbranch Bow, Breastplate of Valor, Deathbringer, Berserker''s Shield, Musashi''s
    Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.38
      fit: 1.0
    Transcendence:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.11
      fit: 0.91
    The Crusher:
      total: 0.66
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 1.0
    Heartseeker:
      total: 0.59
      efficiency: 0.41
      win: 0.59
      pick: 0.5
      fit: 1.0
    Titan's Bane:
      total: 0.63
      efficiency: 0.45
      win: 0.71
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
  - Transcendence
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Breastplate of Valor, The Reaper, Runeforged Hammer, Damaru, Transcendence,
    Pendulum Blade, Lernaean Bow, Arondight, Oni Hunter''s Garb, Berserker''s Shield,
    Golden Blade, Freya''s Tears, Tekko-Kagi, Avenging Blade, Dominance, Kinetic Cuirass,
    Shield Splitter, Amanita Charm, Shield of the Phoenix, Eye of the Storm, Tyrfing,
    Eye of Providence, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.38
      fit: 0.71
    Transcendence:
      total: 0.5
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 0.57
    Heartseeker:
      total: 0.54
      efficiency: 0.41
      win: 0.59
      pick: 0.5
      fit: 0.67
    Titan's Bane:
      total: 0.56
      efficiency: 0.45
      win: 0.71
      pick: 0.28
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Transcendence
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
    god: Genji''s Guard, The Reaper, Pendulum Blade, Breastplate of Valor, Runeforged
    Hammer, Freya''s Tears, Tekko-Kagi, Riptalon, Arondight, Damaru, Silverbranch
    Bow, Shield of the Phoenix, Berserker''s Shield, Lernaean Bow, Kinetic Cuirass,
    Amanita Charm, Screeching Gargoyle, Golden Blade, Chandra''s Grace, Eye of Providence,
    Transcendence, Avenging Blade, Oni Hunter''s Garb, Avatar''s Parashu.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.5
      pick: 0.38
      fit: 0.78
    Transcendence:
      total: 0.48
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.22
    The Crusher:
      total: 0.61
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 0.66
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.59
      pick: 0.5
      fit: 0.66
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.71
      pick: 0.28
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Reaper, Berserker''s
    Shield, Runeforged Hammer, Genji''s Guard, Oni Hunter''s Garb, Eye of the Storm,
    Chandra''s Grace, Erosion, Shield Splitter, Phoenix Feather, Freya''s Tears, Eye
    of Providence, Spectral Armor, Draconic Scale, Riptalon, Breastplate of Valor,
    Golden Blade, Pharaoh''s Curse, Avenging Blade, Leviathan''s Hide, Midgardian
    Mail, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.73
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 0.5
    Titan's Bane:
      total: 0.55
      efficiency: 0.45
      win: 0.71
      pick: 0.28
      fit: 0.4
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.58
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
  - Heartseeker
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
    for this god: The Reaper, Tekko-Kagi, Pendulum Blade, Riptalon, Avenging Blade,
    Silverbranch Bow, Avatar''s Parashu, Runeforged Hammer, Genji''s Guard, Damaru,
    Toxic Blade, Lernaean Bow, Screeching Gargoyle, Golden Blade, Transcendence, Breastplate
    of Valor, Berserker''s Shield, Shield Splitter, Eye of the Storm, Stone of Binding,
    Tyrfing, Oath-Sworn Spear, Arondight, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.38
      fit: 1.0
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.11
      fit: 0.94
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.66
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 1.0
    Heartseeker:
      total: 0.59
      efficiency: 0.41
      win: 0.59
      pick: 0.5
      fit: 1.0
    Titan's Bane:
      total: 0.63
      efficiency: 0.45
      win: 0.71
      pick: 0.28
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Tyrfing
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Golden Blade, Silverbranch Bow, Tyrfing, Berserker''s Shield,
    Lernaean Bow, Toxic Blade, Tekko-Kagi, The Reaper, Genji''s Guard, Pharaoh''s
    Curse, Dominance, Runeforged Hammer, Breastplate of Valor, Damaru, Shogun''s Ofuda,
    Kinetic Cuirass, Amanita Charm, Qin''s Blade, Eye of Providence, Oni Hunter''s
    Garb, Eros'' Bow, Freya''s Tears, Transcendence, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.69
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.58
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.57
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Freya's Tears
  - Titan's Bane
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Shield of the Phoenix, Pendulum Blade, Arondight, Screeching Gargoyle,
    Chandra''s Grace, The Reaper, Gladiator''s Shield, Runeforged Hammer, Berserker''s
    Shield, Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita Charm, Riptalon, Eye
    of Providence, Oni Hunter''s Garb, Regrowth Striders, Lernaean Bow, Silverbranch
    Bow, Golden Blade, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.38
      fit: 0.85
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 0.45
    Titan's Bane:
      total: 0.54
      efficiency: 0.45
      win: 0.71
      pick: 0.28
      fit: 0.35
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
    Underrated for this god: The Reaper, Pendulum Blade, Tekko-Kagi, Runeforged Hammer,
    Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence, Avenging
    Blade, Arondight, Shield Splitter, Genji''s Guard, Eye of the Storm, Tyrfing,
    Riptalon, Dominance, Silverbranch Bow, Breastplate of Valor, Deathbringer, Berserker''s
    Shield, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.38
      fit: 1.0
    Transcendence:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.46
      pick: 0.35
      fit: 0.71
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.11
      fit: 0.91
    The Crusher:
      total: 0.66
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 1.0
    Heartseeker:
      total: 0.59
      efficiency: 0.41
      win: 0.59
      pick: 0.5
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: hybrid
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: The Reaper, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence,
    Avenging Blade, Arondight, Shield Splitter, Genji''s Guard, Eye of the Storm,
    Tyrfing, Riptalon, Dominance, Silverbranch Bow, Breastplate of Valor, Deathbringer,
    Berserker''s Shield, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.5
      pick: 0.38
      fit: 1.0
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.46
      pick: 0.35
      fit: 0.71
    The Reaper:
      total: 0.59
      efficiency: 0.52
      win: 0.58
      pick: 0.11
      fit: 0.91
    The Crusher:
      total: 0.66
      efficiency: 0.64
      win: 0.61
      pick: 0.17
      fit: 1.0
    Heartseeker:
      total: 0.59
      efficiency: 0.41
      win: 0.59
      pick: 0.5
      fit: 1.0
    Titan's Bane:
      total: 0.63
      efficiency: 0.45
      win: 0.71
      pick: 0.28
      fit: 0.91
  swaps:
  - added: Titan's Bane
    removed: Transcendence
    reason: community 71% win over 39 matches (vs 54% on this god), taking the model's
      weakest slot from Transcendence
  starter: *id001
---
