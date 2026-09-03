---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.5
  slot_order:
  - name: Transcendence
    pick_rate: 0.31
    win_rate: 0.49
    alternates:
    - name: Tyrfing
      pick_rate: 0.25
      win_rate: 0.5
    - name: Daybreak Gavel
      pick_rate: 0.14
      win_rate: 0.48
  - name: Jotunn's Revenge
    pick_rate: 0.26
    win_rate: 0.48
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.13
      win_rate: 0.53
    - name: Toxic Blade
      pick_rate: 0.08
      win_rate: 0.62
  - name: Odysseus' Bow
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: The Crusher
      pick_rate: 0.13
      win_rate: 0.56
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.48
  - name: Heartseeker
    pick_rate: 0.13
    win_rate: 0.49
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.63
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.49
  - name: Titan's Bane
    pick_rate: 0.14
    win_rate: 0.52
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.67
    - name: The Executioner
      pick_rate: 0.06
      win_rate: 0.26
  - name: Avatar's Parashu
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.07
      win_rate: 0.4
    - name: Axe
      pick_rate: 0.07
      win_rate: 0.71
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.49
  - name: Leather Cowl
    pick_rate: 0.14
    win_rate: 0.44
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-09-02'
  god_win_rate: 0.5042735042735043
  god_matches_won: 177
  god_matches_played: 351
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-01'
  god_matches_analyzed: 8200
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Hydra''s
    Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Musashi''s Dual Swords,
    Arondight, Pendulum Blade, Damaru, Rage, Runeforged Hammer, Qin''s Blade, Berserker''s
    Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.47
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.44
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.5
      pick: 0.25
      fit: 0.57
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.49
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.44
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.34
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Crusher
  - Avatar's Parashu
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Toxic
    Blade, Hydra''s Lament, Lernaean Bow, The Reaper, Tekko-Kagi, Riptalon, Dominance,
    Deathbringer, Golden Blade, Arondight, Musashi''s Dual Swords, Demon Blade, Runeforged
    Hammer, Pendulum Blade, Damaru, Rage, Avenging Blade, Qin''s Blade, Barbed Carver,
    Berserker''s Shield, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Toxic Blade:
      total: 0.48
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.32
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.44
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.49
      pick: 0.31
      fit: 0.24
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.48
      efficiency: 0.47
      win: 0.49
      pick: 0.22
      fit: 0.55
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.29
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  - Avatar's Parashu
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, The Reaper, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords,
    Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.46
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.45
      efficiency: 0.46
      win: 0.51
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.46
      efficiency: 0.38
      win: 0.51
      pick: 0.0
      fit: 0.64
    Deathbringer:
      total: 0.47
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.32
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - The Reaper
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Toxic Blade, The Reaper, Riptalon, Tekko-Kagi, Hydra''s Lament, Lernaean
    Bow, Deathbringer, Pendulum Blade, Dominance, Golden Blade, Arondight, Musashi''s
    Dual Swords, Demon Blade, Runeforged Hammer, Damaru, Rage, Qin''s Blade, Avenging
    Blade, Berserker''s Shield, Breastplate of Valor, Barbed Carver, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.46
    The Reaper:
      total: 0.48
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.49
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.43
    Titan's Bane:
      total: 0.48
      efficiency: 0.47
      win: 0.52
      pick: 0.3
      fit: 0.43
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.33
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Toxic Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Toxic Blade, Riptalon, The Reaper,
    Shield of the Phoenix, Kinetic Cuirass, Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Runeforged Hammer, Golden Blade, Yogi''s Necklace, Shifter''s Shield,
    Shield Splitter, Lernaean Bow, Pharaoh''s Curse, Hydra''s Lament, Chandra''s Grace,
    Shogun''s Ofuda, Phoenix Feather, Eye of the Storm, Tekko-Kagi, Erosion, Eye of
    Providence, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.46
      win: 0.62
      pick: 0.11
      fit: 0.44
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.3
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.68
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.23
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - The Executioner
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - The Executioner
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Toxic Blade, Riptalon, The Reaper, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Avenging Blade, Deathbringer, Pendulum Blade, Golden Blade, Dominance,
    Demon Blade, Musashi''s Dual Swords, Arondight, Oath-Sworn Spear, Runeforged Hammer,
    Damaru, Rage, Qin''s Blade, Berserker''s Shield, Screeching Gargoyle.'
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.56
    The Executioner:
      total: 0.51
      efficiency: 0.35
      win: 0.63
      pick: 0.2
      fit: 0.6
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.53
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.51
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.55
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.45
  community_ordered:
  - Toxic Blade
  - The Executioner
  - Jotunn's Revenge
  - The Crusher
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Lernaean Bow, Tekko-Kagi, The Reaper, Golden
    Blade, Hydra''s Lament, Deathbringer, Dominance, Qin''s Blade, Demon Blade, Musashi''s
    Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade, Dagger of Frenzy, Barbed Carver.'
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.52
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.35
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.25
      fit: 0.6
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.49
      pick: 0.18
      fit: 0.52
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.26
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - The Crusher
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Toxic Blade, Hydra''s Lament, Riptalon,
    Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Pendulum Blade, Deathbringer,
    Dominance, Golden Blade, Breastplate of Valor, Musashi''s Dual Swords, Genji''s
    Guard, Demon Blade, Qin''s Blade, Runeforged Hammer, Berserker''s Shield, Damaru,
    Rage, Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.49
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.46
    Arondight:
      total: 0.46
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.47
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.31
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.21
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - The Reaper
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Hydra''s
    Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Toxic Blade, Musashi''s
    Dual Swords, Arondight, Pendulum Blade, Damaru, Rage, Runeforged Hammer, Qin''s
    Blade, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.44
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.56
    Silverbranch Bow:
      total: 0.48
      efficiency: 0.53
      win: 0.49
      pick: 0.18
      fit: 0.47
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.49
      win: 0.51
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Jotunn's Revenge
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - Toxic Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Toxic Blade, Hydra''s Lament, Deathbringer, Riptalon, Tekko-Kagi,
    Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight, Damaru, Rage,
    Demon Blade, Golden Blade, Dominance, Runeforged Hammer, Barbed Carver, Avenging
    Blade, Bloodforge, Qin''s Blade, Shield Splitter, Breastplate of Valor.'
  slot_scores:
    Toxic Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.53
    The Reaper:
      total: 0.5
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.5
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.51
    Titan's Bane:
      total: 0.49
      efficiency: 0.47
      win: 0.52
      pick: 0.3
      fit: 0.51
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.41
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, The Reaper, Toxic Blade, Deathbringer, Lernaean Bow, Tekko-Kagi, Riptalon,
    Arondight, Musashi''s Dual Swords, Dominance, Pendulum Blade, Runeforged Hammer,
    Golden Blade, Damaru, Rage, Avenging Blade, Demon Blade, Barbed Carver, Breastplate
    of Valor, Bloodforge, Genji''s Guard, Shield Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.5
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.49
      pick: 0.31
      fit: 0.27
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.49
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.43
    Heartseeker:
      total: 0.48
      efficiency: 0.47
      win: 0.49
      pick: 0.22
      fit: 0.6
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  - Avatar's Parashu
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, The Reaper, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords,
    Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.46
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.45
      efficiency: 0.46
      win: 0.51
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.46
      efficiency: 0.38
      win: 0.51
      pick: 0.0
      fit: 0.64
    Deathbringer:
      total: 0.47
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.32
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - Toxic Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Toxic Blade, Hydra''s Lament, Riptalon, Tekko-Kagi, Deathbringer,
    Pendulum Blade, Lernaean Bow, Arondight, Musashi''s Dual Swords, Runeforged Hammer,
    Golden Blade, Dominance, Damaru, Rage, Demon Blade, Avenging Blade, Barbed Carver,
    Breastplate of Valor, Genji''s Guard, Bloodforge, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.53
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.5
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.48
    Titan's Bane:
      total: 0.49
      efficiency: 0.47
      win: 0.52
      pick: 0.3
      fit: 0.48
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.38
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Toxic Blade
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Berserker''s Shield, Shield of the Phoenix,
    Riptalon, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Erosion, Shifter''s Shield, Yogi''s Necklace, Shield Splitter,
    Pharaoh''s Curse, Eye of the Storm, Umbral Link, Golden Blade, Phoenix Feather,
    Chandra''s Grace, Hydra''s Lament, Shogun''s Ofuda, Eye of Providence, Void Shield,
    Stampede, Draconic Scale, Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.46
      win: 0.62
      pick: 0.11
      fit: 0.37
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.34
    The Reaper:
      total: 0.52
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.63
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.26
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Toxic Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Toxic Blade, Riptalon, Tekko-Kagi, Hydra''s Lament,
    Pendulum Blade, Avenging Blade, Deathbringer, Lernaean Bow, Musashi''s Dual Swords,
    Arondight, Oath-Sworn Spear, Damaru, Rage, Golden Blade, Runeforged Hammer, Dominance,
    Demon Blade, Barbed Carver, Screeching Gargoyle, Bloodforge.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.62
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.52
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.63
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.52
      pick: 0.3
      fit: 0.63
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.53
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Lernaean Bow, Tekko-Kagi, The Reaper, Golden
    Blade, Hydra''s Lament, Deathbringer, Dominance, Qin''s Blade, Demon Blade, Musashi''s
    Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade, Dagger of Frenzy, Barbed Carver.'
  slot_scores:
    Toxic Blade:
      total: 0.52
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.52
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.35
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.25
      fit: 0.6
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.49
      pick: 0.18
      fit: 0.52
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.26
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Silverbranch Bow
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Toxic Blade
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Toxic Blade, The
    Reaper, Arondight, Pendulum Blade, Riptalon, Deathbringer, Lernaean Bow, Tekko-Kagi,
    Breastplate of Valor, Musashi''s Dual Swords, Genji''s Guard, Runeforged Hammer,
    Golden Blade, Damaru, Rage, Dominance, Demon Blade, Avenging Blade, Eye of Erebus,
    Barbed Carver, Daybreak Gavel.'
  slot_scores:
    Toxic Blade:
      total: 0.48
      efficiency: 0.44
      win: 0.62
      pick: 0.11
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.57
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.52
    Arondight:
      total: 0.47
      efficiency: 0.5
      win: 0.51
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.48
      efficiency: 0.47
      win: 0.56
      pick: 0.2
      fit: 0.35
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.45
      win: 0.75
      pick: 0.25
      fit: 0.25
  community_ordered:
  - Toxic Blade
  - Jotunn's Revenge
  - The Crusher
  - Avatar's Parashu
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Deathbringer
  - Heartseeker
  flex_slots:
  - Deathbringer
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
    Underrated for this god: The Reaper, Hydra''s Lament, Deathbringer, Riptalon,
    Tekko-Kagi, Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight, Damaru,
    Rage, Demon Blade, Golden Blade, Dominance, Runeforged Hammer, Toxic Blade, Barbed
    Carver, Avenging Blade, Bloodforge, Qin''s Blade, Shield Splitter, Breastplate
    of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.48
      pick: 0.35
      fit: 0.53
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.49
      pick: 0.31
      fit: 0.2
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.51
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.5
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.53
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.49
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.49
      pick: 0.22
      fit: 0.61
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
