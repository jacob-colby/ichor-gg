---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.42
  aspect_win_rate: 0.56
  slot_order:
  - name: Tyrfing
    pick_rate: 0.43
    win_rate: 0.61
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.26
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.47
  - name: Hastened Fatalis
    pick_rate: 0.18
    win_rate: 0.62
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.58
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.38
  - name: Sun Beam Bow
    pick_rate: 0.13
    win_rate: 0.72
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.14
      win_rate: 0.6
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.33
  - name: Odysseus' Bow
    pick_rate: 0.12
    win_rate: 0.65
    alternates:
    - name: Totem of Death
      pick_rate: 0.11
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.27
  - name: The Executioner
    pick_rate: 0.13
    win_rate: 0.65
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.64
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.55
  - name: Blinking Abyss
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.67
    - name: Hunter's Bow
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.25
    win_rate: 0.64
  - name: Death's Embrace
    pick_rate: 0.18
    win_rate: 0.62
  - name: Hunter's Cowl
    pick_rate: 0.12
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-15'
  god_win_rate: 0.5211267605633803
  god_matches_won: 74
  god_matches_played: 142
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Gluttonous Grimoire
  - Death Metal
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Nimble Ring, Gluttonous Grimoire, Death
    Metal, Berserker''s Shield, Damaru, Lernaean Bow, Golden Blade, Soul Gem, Tekko-Kagi,
    Hydra''s Lament, Riptalon, The Reaper, Genji''s Guard, Bragi''s Harp, Runeforged
    Hammer, The Cosmic Horror, Dominance, Spear of the Magus, Breastplate of Valor,
    Pharaoh''s Curse, Demon Blade, Heartseeker, Bracer of The Abyss, Titan''s Bane,
    Deathbringer, Kinetic Cuirass, Amanita Charm, Transcendence, Avenging Blade, Toxic
    Blade, Pendulum Blade, Shield Splitter, Eye of Providence, Oni Hunter''s Garb,
    Spear of Desolation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.46
      win: 0.61
      pick: 0.43
      fit: 0.59
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.36
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.45
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.55
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Nimble Ring, The Crusher, Gluttonous Grimoire, Soul Gem, Death Metal,
    Genji''s Guard, Hydra''s Lament, The Cosmic Horror, Berserker''s Shield, Spear
    of the Magus, Breastplate of Valor, Damaru, Bragi''s Harp, Lernaean Bow, Golden
    Blade, Runeforged Hammer, Chronos'' Pendant, The Reaper, Bracer of The Abyss,
    Dominance, Riptalon, Tekko-Kagi, Bancroft''s Talon, Oni Hunter''s Garb, Helm of
    Radiance, Doom Orb, Transcendence, The World Stone, Blood-Bound Book, Rod of Asclepius,
    Heartseeker, Kinetic Cuirass, Freya''s Tears, Amanita Charm, Gem of Focus, Spear
    of Desolation.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.44
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.28
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Silverbranch Bow
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Soul Gem,
    Gluttonous Grimoire, Kinetic Cuirass, The Crusher, Riptalon, The Reaper, Nimble
    Ring, Jotunn''s Revenge, Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Pharaoh''s
    Curse, Oni Hunter''s Garb, Golden Blade, Runeforged Hammer, Phoenix Feather, Freya''s
    Tears, Breastplate of Valor, Spectral Armor, Death Metal, Blood-Bound Book, Erosion,
    Shogun''s Ofuda, Shifter''s Shield, Eye of the Storm, Damaru, Shield Splitter,
    Eye of Providence, Hydra''s Lament, Bancroft''s Talon, Lernaean Bow, Draconic
    Scale, Lifebinder, Leviathan''s Hide, Midgardian Mail, The Cosmic Horror, Avenging
    Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.27
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tyrfing
  - Tekko-Kagi
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem, Nimble
    Ring, Riptalon, Tekko-Kagi, The Cosmic Horror, The Reaper, Spear of the Magus,
    Berserker''s Shield, Avenging Blade, Death Metal, Damaru, Lernaean Bow, Genji''s
    Guard, Heartseeker, Hydra''s Lament, Golden Blade, Titan''s Bane, Toxic Blade,
    Screeching Gargoyle, Runeforged Hammer, Pendulum Blade, Breastplate of Valor,
    Doom Orb, Bragi''s Harp, Stone of Binding, The World Stone, Dominance, Kinetic
    Cuirass, Pharaoh''s Curse, Void Shield, Amanita Charm, Dreamer''s Idol, Avatar''s
    Parashu, Spear of Desolation.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.61
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.61
      pick: 0.43
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.57
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Golden Blade
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
    this god: Nimble Ring, Riptalon, The Crusher, Gluttonous Grimoire, Golden Blade,
    Jotunn''s Revenge, Berserker''s Shield, Soul Gem, Lernaean Bow, Genji''s Guard,
    Death Metal, Damaru, Toxic Blade, The Reaper, Hydra''s Lament, Tekko-Kagi, The
    Cosmic Horror, Pharaoh''s Curse, Runeforged Hammer, Breastplate of Valor, Spear
    of the Magus, Bragi''s Harp, Dominance, Bracer of The Abyss, Kinetic Cuirass,
    Amanita Charm, Eye of Providence, Shogun''s Ofuda, Oni Hunter''s Garb, Blood-Bound
    Book, Freya''s Tears, Eros'' Bow, Bancroft''s Talon, Qin''s Blade, Demon Blade,
    Transcendence, Spear of Desolation.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.57
    Tyrfing:
      total: 0.56
      efficiency: 0.46
      win: 0.61
      pick: 0.43
      fit: 0.67
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.57
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Genji''s
    Guard, Nimble Ring, Hydra''s Lament, The Crusher, Breastplate of Valor, Gluttonous
    Grimoire, Chronos'' Pendant, Freya''s Tears, Berserker''s Shield, Shield of the
    Phoenix, Death Metal, The Cosmic Horror, Screeching Gargoyle, Gem of Focus, Chandra''s
    Grace, Spear of the Magus, Damaru, Riptalon, Arondight, Lernaean Bow, Pendulum
    Blade, Golden Blade, Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Bracer
    of The Abyss, The Reaper, Bragi''s Harp, Pharaoh''s Curse, Tekko-Kagi, Eye of
    Providence, Oni Hunter''s Garb, Gladiator''s Shield, Spear of Desolation.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.31
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.34
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Berserker's Shield
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
    Underrated for this god: The Crusher, Jotunn''s Revenge, Nimble Ring, Gluttonous
    Grimoire, Death Metal, Berserker''s Shield, Damaru, Lernaean Bow, Golden Blade,
    Soul Gem, Tekko-Kagi, Hydra''s Lament, Riptalon, The Reaper, Genji''s Guard, Bragi''s
    Harp, Runeforged Hammer, The Cosmic Horror, Dominance, Spear of the Magus, Breastplate
    of Valor, Pharaoh''s Curse, Spear of Desolation, Demon Blade, Heartseeker, Bracer
    of The Abyss, Titan''s Bane, Deathbringer, Kinetic Cuirass, Amanita Charm, Transcendence,
    Avenging Blade, Toxic Blade, Pendulum Blade, Shield Splitter, Eye of Providence,
    Oni Hunter''s Garb.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.31
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.44
      efficiency: 0.77
      win: 0.27
      pick: 0.18
      fit: 0.26
  starter: *id001
---
