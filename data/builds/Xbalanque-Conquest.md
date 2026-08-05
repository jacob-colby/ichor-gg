---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.57
  slot_order:
  - name: Tyrfing
    pick_rate: 0.48
    win_rate: 0.63
    alternates:
    - name: Dominance
      pick_rate: 0.13
      win_rate: 0.64
    - name: Transcendence
      pick_rate: 0.11
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.38
    win_rate: 0.6
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.1
      win_rate: 0.66
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.61
  - name: Dominance
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.21
      win_rate: 0.7
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 0.49
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.69
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.62
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.61
  - name: Qin's Blade
    pick_rate: 0.1
    win_rate: 0.81
    alternates:
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.54
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.61
  - name: Riptalon
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Manchu Bow
      pick_rate: 0.12
      win_rate: 0.71
    - name: Hunter's Bow
      pick_rate: 0.11
      win_rate: 0.46
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-08-01'
  god_win_rate: 0.6
  god_matches_won: 201
  god_matches_played: 335
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Dominance
  - Qin's Blade
  - Riptalon
  flex_slots:
  - Berserker's Shield
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Berserker''s Shield, Lernaean Bow, Damaru, Golden Blade, The
    Crusher, Demon Blade, Jotunn''s Revenge, Hydra''s Lament, Runeforged Hammer, Pharaoh''s
    Curse, Genji''s Guard, Tekko-Kagi, Silverbranch Bow, The Reaper, Musashi''s Dual
    Swords, Shogun''s Ofuda, Amanita Charm, Breastplate of Valor, Oni Hunter''s Garb,
    Eros'' Bow, Yogi''s Necklace, Avenging Blade, Kinetic Cuirass, Rage, Shield Splitter,
    Eye of Providence.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Tyrfing:
      total: 0.57
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.64
    Dominance:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.18
      fit: 0.54
    Qin's Blade:
      total: 0.57
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.43
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.46
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Qin's Blade
  - Musashi's Dual Swords
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Damaru, Berserker''s Shield, Lernaean Bow, The Crusher, Golden
    Blade, Demon Blade, Jotunn''s Revenge, Hydra''s Lament, Runeforged Hammer, Genji''s
    Guard, Pharaoh''s Curse, Musashi''s Dual Swords, Tekko-Kagi, The Reaper, Silverbranch
    Bow, Amanita Charm, Rage, Shogun''s Ofuda, Breastplate of Valor, Oni Hunter''s
    Garb, Yogi''s Necklace, Kinetic Cuirass, Avenging Blade, Eros'' Bow, Eye of Providence,
    Shield Splitter.'
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.6
    Qin's Blade:
      total: 0.56
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.4
    Musashi's Dual Swords:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.42
    Damaru:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.49
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Dominance
  - Qin's Blade
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Dominance
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Amanita Charm, Berserker''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, Genji''s
    Guard, Runeforged Hammer, Golden Blade, The Reaper, The Crusher, Lernaean Bow,
    Damaru, Shogun''s Ofuda, Chandra''s Grace, Shifter''s Shield, Yogi''s Necklace,
    Phoenix Feather, Spectral Armor, Jotunn''s Revenge, Breastplate of Valor, Hydra''s
    Lament, Erosion, Eye of the Storm, Freya''s Tears, Shield Splitter, Umbral Link.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.42
    Dominance:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.18
      fit: 0.32
    Qin's Blade:
      total: 0.55
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.3
    Riptalon:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.58
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Qin's Blade
  - Riptalon
  - The Crusher
  flex_slots:
  - Dominance
  - Jotunn's Revenge
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Riptalon, The Crusher, Jotunn''s Revenge, Berserker''s Shield, Silverbranch
    Bow, The Reaper, Tekko-Kagi, Lernaean Bow, Damaru, Avenging Blade, Genji''s Guard,
    Hydra''s Lament, Golden Blade, Heartseeker, Runeforged Hammer, Pharaoh''s Curse,
    Titan''s Bane, Toxic Blade, Screeching Gargoyle, Amanita Charm, Breastplate of
    Valor, Oni Hunter''s Garb, Stone of Binding, Yogi''s Necklace, Kinetic Cuirass,
    Void Shield, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.46
    Dominance:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.18
      fit: 0.36
    Qin's Blade:
      total: 0.55
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.32
    Riptalon:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.64
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Dominance
  - Qin's Blade
  - Riptalon
  flex_slots:
  - Berserker's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Qin''s Blade, Berserker''s Shield, Golden Blade, Lernaean
    Bow, Damaru, The Crusher, Silverbranch Bow, Jotunn''s Revenge, Genji''s Guard,
    Hydra''s Lament, Runeforged Hammer, Pharaoh''s Curse, Demon Blade, Amanita Charm,
    Breastplate of Valor, Oni Hunter''s Garb, Shogun''s Ofuda, Tekko-Kagi, Yogi''s
    Necklace, Kinetic Cuirass, The Reaper, Eros'' Bow, Toxic Blade, Avenging Blade,
    Eye of Providence, Musashi''s Dual Swords.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.59
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.75
    Dominance:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.18
      fit: 0.45
    Qin's Blade:
      total: 0.59
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.59
    Riptalon:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Qin's Blade
  - Riptalon
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Riptalon, Genji''s Guard, Jotunn''s
    Revenge, Hydra''s Lament, Berserker''s Shield, Breastplate of Valor, The Crusher,
    Lernaean Bow, Damaru, Freya''s Tears, Shield of the Phoenix, Runeforged Hammer,
    Golden Blade, Arondight, Screeching Gargoyle, Chandra''s Grace, Pharaoh''s Curse,
    Amanita Charm, Oni Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Silverbranch
    Bow, Eye of Providence, Shogun''s Ofuda, The Reaper, Demon Blade, Eros'' Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.53
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.4
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Qin's Blade:
      total: 0.55
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.31
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Dominance
  - Qin's Blade
  - Riptalon
  flex_slots:
  - Death Metal
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Riptalon, Gluttonous Grimoire, Soul Gem,
    Death Metal, Jotunn''s Revenge, The Crusher, Berserker''s Shield, Genji''s Guard,
    Spear of the Magus, Hydra''s Lament, The Cosmic Horror, Bracer of The Abyss, Lernaean
    Bow, Spear of Desolation, Damaru, Bragi''s Harp, Blood-Bound Book, Breastplate
    of Valor, Chronos'' Pendant, Bancroft''s Talon, Runeforged Hammer, Obsidian Shard,
    Rod of Asclepius, Nimble Ring, Golden Blade, Silverbranch Bow, The Reaper, Helm
    of Radiance, Amanita Charm, Jade Scepter, Pharaoh''s Curse, Oni Hunter''s Garb,
    Yogi''s Necklace, Gem of Focus, Kinetic Cuirass, Tekko-Kagi, Dreamer''s Idol,
    The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.53
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Dominance:
      total: 0.52
      efficiency: 0.53
      win: 0.63
      pick: 0.18
      fit: 0.29
    Qin's Blade:
      total: 0.54
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.28
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Tyrfing
  - Death Metal
  - Dominance
  - Qin's Blade
  - Riptalon
  - The Crusher
  flex_slots:
  - Death Metal
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Riptalon, Gluttonous Grimoire, Death
    Metal, The Crusher, Soul Gem, Jotunn''s Revenge, Berserker''s Shield, Lernaean
    Bow, Damaru, Spear of the Magus, Bragi''s Harp, Bracer of The Abyss, Hydra''s
    Lament, The Cosmic Horror, Runeforged Hammer, Golden Blade, Genji''s Guard, The
    Reaper, Blood-Bound Book, Silverbranch Bow, Bancroft''s Talon, Tekko-Kagi, Nimble
    Ring, Obsidian Shard, Rod of Asclepius, Spear of Desolation, Pharaoh''s Curse,
    Amanita Charm, Helm of Radiance, Breastplate of Valor, Oni Hunter''s Garb, Jade
    Scepter, Heartseeker, Yogi''s Necklace, Kinetic Cuirass, Chronos'' Pendant, Demon
    Blade, Avenging Blade.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.47
      win: 0.63
      pick: 0.48
      fit: 0.48
    Death Metal:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.57
    Dominance:
      total: 0.54
      efficiency: 0.53
      win: 0.63
      pick: 0.18
      fit: 0.38
    Qin's Blade:
      total: 0.55
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.3
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.13
      fit: 0.43
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Dominance
  - Damaru
  - The Crusher
  flex_slots:
  - The Crusher
  - Dominance
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Lernaean Bow, Damaru, Golden Blade,
    The Crusher, Demon Blade, Riptalon, Jotunn''s Revenge, Hydra''s Lament, Runeforged
    Hammer, Pharaoh''s Curse, Genji''s Guard, Tekko-Kagi, Silverbranch Bow, The Reaper,
    Musashi''s Dual Swords, Shogun''s Ofuda, Amanita Charm, Breastplate of Valor,
    Oni Hunter''s Garb, Eros'' Bow, Yogi''s Necklace, Avenging Blade, Kinetic Cuirass,
    Rage, Shield Splitter, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Dominance:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.18
      fit: 0.54
    Damaru:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Qin's Blade
  - Damaru
  - The Crusher
  flex_slots:
  - The Crusher
  - Qin's Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Lernaean Bow,
    Damaru, Golden Blade, The Crusher, Demon Blade, Riptalon, Jotunn''s Revenge, Hydra''s
    Lament, Runeforged Hammer, Pharaoh''s Curse, Genji''s Guard, Tekko-Kagi, Silverbranch
    Bow, The Reaper, Musashi''s Dual Swords, Shogun''s Ofuda, Amanita Charm, Breastplate
    of Valor, Oni Hunter''s Garb, Eros'' Bow, Yogi''s Necklace, Avenging Blade, Kinetic
    Cuirass, Rage, Shield Splitter, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Qin's Blade:
      total: 0.57
      efficiency: 0.38
      win: 0.81
      pick: 0.1
      fit: 0.43
    Damaru:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
  swaps:
  - added: Qin's Blade
    removed: Dominance
    reason: community 81% win over 34 matches (vs 60% on this god), taking the model's
      weakest slot from Dominance
  starter: *id001
---
