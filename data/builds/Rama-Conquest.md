---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.6
  slot_order:
  - name: Tyrfing
    pick_rate: 0.64
    win_rate: 0.53
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.56
    - name: Avenging Blade
      pick_rate: 0.07
      win_rate: 0.54
  - name: Odysseus' Bow
    pick_rate: 0.31
    win_rate: 0.52
    alternates:
    - name: Toxic Blade
      pick_rate: 0.16
      win_rate: 0.62
    - name: Dagger of Frenzy
      pick_rate: 0.11
      win_rate: 0.5
  - name: Silverbranch Bow
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.16
      win_rate: 0.64
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.49
  - name: The Executioner
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.22
      win_rate: 0.54
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.52
  - name: Riptalon
    pick_rate: 0.12
    win_rate: 0.56
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.62
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.52
  - name: Manchu Bow
    pick_rate: 0.12
    win_rate: 0.53
    alternates:
    - name: Bow
      pick_rate: 0.11
      win_rate: 0.52
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.57
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.35
    win_rate: 0.57
  - name: Hunter's Cowl
    pick_rate: 0.19
    win_rate: 0.63
  - name: Gilded Arrow
    pick_rate: 0.17
    win_rate: 0.41
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-08-22'
  god_win_rate: 0.5355029585798816
  god_matches_won: 362
  god_matches_played: 676
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - The Crusher
  flex_slots:
  - Toxic Blade
  - The Crusher
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Berserker''s Shield, The Crusher, Lernaean Bow, Tekko-Kagi,
    The Reaper, Golden Blade, Heartseeker, Deathbringer, Damaru, Runeforged Hammer,
    Demon Blade, Hydra''s Lament, Dominance, Genji''s Guard, Breastplate of Valor,
    Titan''s Bane, Pharaoh''s Curse, Amanita Charm, Musashi''s Dual Swords, Kinetic
    Cuirass, Shogun''s Ofuda, Avenging Blade, Freya''s Tears, Shield Splitter, Eye
    of Providence.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.46
      win: 0.62
      pick: 0.22
      fit: 0.42
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.53
      pick: 0.64
      fit: 0.54
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.26
      fit: 0.52
    The Crusher:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.44
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Berserker''s Shield, The Crusher, Hydra''s Lament, Genji''s Guard, Breastplate
    of Valor, Lernaean Bow, Heartseeker, The Reaper, Runeforged Hammer, Tekko-Kagi,
    Golden Blade, Dominance, Amanita Charm, Freya''s Tears, Deathbringer, Damaru,
    Kinetic Cuirass, Titan''s Bane, Avenging Blade, Transcendence, Shield Splitter,
    Pharaoh''s Curse, Arondight, Eye of Providence, Musashi''s Dual Swords, Shield
    of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.53
      pick: 0.64
      fit: 0.44
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Damaru
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Damaru
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Berserker''s Shield, The Crusher, Lernaean Bow, Tekko-Kagi,
    The Reaper, Deathbringer, Damaru, Golden Blade, Heartseeker, Demon Blade, Runeforged
    Hammer, Genji''s Guard, Hydra''s Lament, Breastplate of Valor, Dominance, Musashi''s
    Dual Swords, Amanita Charm, Pharaoh''s Curse, Titan''s Bane, Kinetic Cuirass,
    Shogun''s Ofuda, Freya''s Tears, Rage, Shield Splitter, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.53
      pick: 0.64
      fit: 0.5
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.26
      fit: 0.5
    Damaru:
      total: 0.48
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.46
    Demon Blade:
      total: 0.48
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.7
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Tyrfing
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Berserker''s Shield, The Reaper, Genji''s
    Guard, Breastplate of Valor, Tekko-Kagi, Hydra''s Lament, Heartseeker, Lernaean
    Bow, Freya''s Tears, Runeforged Hammer, Titan''s Bane, Amanita Charm, Golden Blade,
    Kinetic Cuirass, Deathbringer, Damaru, Shield of the Phoenix, Pharaoh''s Curse,
    Pendulum Blade, Dominance, Arondight, Eye of Providence, Screeching Gargoyle,
    Shield Splitter.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.46
      win: 0.62
      pick: 0.22
      fit: 0.37
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.53
      pick: 0.64
      fit: 0.4
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.26
      fit: 0.43
    The Crusher:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, The Reaper, Kinetic Cuirass, Pharaoh''s Curse, Runeforged Hammer, Freya''s
    Tears, Genji''s Guard, The Crusher, Breastplate of Valor, Shogun''s Ofuda, Yogi''s
    Necklace, Phoenix Feather, Golden Blade, Shifter''s Shield, Shield Splitter, Chandra''s
    Grace, Lernaean Bow, Mantle Of Discord, Stone of Binding, Spectral Armor, Eye
    of the Storm, Erosion, Tekko-Kagi, Leviathan''s Hide, Eye of Providence.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.46
      win: 0.62
      pick: 0.22
      fit: 0.41
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.26
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Tekko-Kagi, Berserker''s
    Shield, Heartseeker, Avenging Blade, Titan''s Bane, Stone of Binding, Lernaean
    Bow, Screeching Gargoyle, Golden Blade, Runeforged Hammer, Genji''s Guard, Breastplate
    of Valor, Hydra''s Lament, Deathbringer, Damaru, Amanita Charm, Avatar''s Parashu,
    Kinetic Cuirass, Dominance, Void Shield, Pharaoh''s Curse, Pendulum Blade, Freya''s
    Tears.'
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.46
      win: 0.62
      pick: 0.22
      fit: 0.53
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.26
      fit: 0.61
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.53
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Berserker''s Shield, Golden Blade, The Crusher, Lernaean
    Bow, Tekko-Kagi, The Reaper, Genji''s Guard, Heartseeker, Breastplate of Valor,
    Runeforged Hammer, Pharaoh''s Curse, Hydra''s Lament, Amanita Charm, Deathbringer,
    Damaru, Dominance, Kinetic Cuirass, Shogun''s Ofuda, Demon Blade, Qin''s Blade,
    Titan''s Bane, Freya''s Tears, Eye of Providence, Musashi''s Dual Swords, Shield
    Splitter.'
  slot_scores:
    Toxic Blade:
      total: 0.53
      efficiency: 0.46
      win: 0.62
      pick: 0.22
      fit: 0.54
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.53
      pick: 0.64
      fit: 0.64
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.56
      pick: 0.26
      fit: 0.62
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.28
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Berserker''s Shield, Hydra''s Lament, Freya''s Tears, The
    Crusher, Shield of the Phoenix, Lernaean Bow, Screeching Gargoyle, The Reaper,
    Arondight, Amanita Charm, Tekko-Kagi, Kinetic Cuirass, Runeforged Hammer, Heartseeker,
    Golden Blade, Pharaoh''s Curse, Pendulum Blade, Deathbringer, Damaru, Eye of Providence,
    Chandra''s Grace, Shogun''s Ofuda, Dominance, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.28
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.08
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - The Reaper
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, The Crusher,
    Lernaean Bow, Tekko-Kagi, The Reaper, Golden Blade, Heartseeker, Deathbringer,
    Damaru, Runeforged Hammer, Demon Blade, Hydra''s Lament, Dominance, Genji''s Guard,
    Breastplate of Valor, Titan''s Bane, Pharaoh''s Curse, Amanita Charm, Musashi''s
    Dual Swords, Kinetic Cuirass, Shogun''s Ofuda, Freya''s Tears, Shield Splitter,
    Avenging Blade, Eye of Providence.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.5
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.44
  starter: *id001
---
