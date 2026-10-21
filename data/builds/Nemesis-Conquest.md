---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.6
  slot_order:
  - name: Hydra's Lament
    pick_rate: 0.37
    win_rate: 0.55
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.2
      win_rate: 0.33
    - name: Jotunn's Revenge
      pick_rate: 0.17
      win_rate: 0.4
  - name: Arondight
    pick_rate: 0.17
    win_rate: 0.6
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.17
      win_rate: 0.8
    - name: Sanguine Lash
      pick_rate: 0.1
      win_rate: 0.33
  - name: Sanguine Lash
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.33
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.21
    win_rate: 0.5
    alternates:
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.33
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.5
  - name: Avatar's Parashu
    pick_rate: 0.19
    win_rate: 0.8
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.67
    - name: Caestus
      pick_rate: 0.07
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.0
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.67
  - name: Hunter's Cowl
    pick_rate: 0.3
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.17
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-10-21'
  god_win_rate: 0.5333333333333333
  god_matches_won: 16
  god_matches_played: 30
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch Bow, Lernaean
    Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus, Riptalon, Spear
    of Desolation, Titan''s Bane, The Reaper, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The World Stone,
    Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient Signet,
    Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.4
      pick: 0.17
      fit: 0.49
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.55
      pick: 0.37
      fit: 0.39
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.35
      fit: 0.64
    Avatar's Parashu:
      total: 0.61
      efficiency: 0.45
      win: 0.8
      pick: 0.41
      fit: 0.44
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Arondight
  - Rod of Tahuti
  - Avatar's Parashu
  flex_slots:
  - Jotunn's Revenge
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom Orb, Tekko-Kagi,
    Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Silverbranch
    Bow, Dominance, Bracer of The Abyss, Titan''s Bane, The Reaper, Golden Blade,
    Dreamer''s Idol, Transcendence, Deathbringer, Gem of Focus, Book of Thoth, Polynomicon,
    Pendulum Blade, Riptalon, Runeforged Hammer, Musashi''s Dual Swords, Soul Reaver,
    Rod of Asclepius, The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.4
      pick: 0.17
      fit: 0.52
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.55
      pick: 0.37
      fit: 0.49
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.54
    Arondight:
      total: 0.5
      efficiency: 0.5
      win: 0.6
      pick: 0.23
      fit: 0.31
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.8
      pick: 0.41
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - Shield of the Phoenix
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, The Reaper, Golden Blade, Death Metal,
    Riptalon, Runeforged Hammer, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard,
    Shifter''s Shield, Breastplate of Valor, Shield Splitter, Ethereal Staff, Yogi''s
    Necklace, Eye of the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix Feather,
    Erosion, Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow, Eye of Providence,
    Spear of the Magus, Tekko-Kagi, Lifebinder, Draconic Scale, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.55
      pick: 0.37
      fit: 0.28
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.6
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.8
      pick: 0.41
      fit: 0.27
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Silverbranch Bow
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Silverbranch Bow, Tekko-Kagi, Spear of the Magus,
    Death Metal, Spear of Desolation, Obsidian Shard, Titan''s Bane, Soul Gem, The
    Reaper, Riptalon, Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean Bow, Doom
    Orb, The World Stone, Nimble Ring, Avenging Blade, Dreamer''s Idol, Pendulum Blade,
    Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic Horror, Bracer
    of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, Transcendence,
    The Executioner, Runeforged Hammer, Ancient Signet, Qin''s Blade, Chronos'' Pendant.'
  slot_scores:
    Book of Thoth:
      total: 0.41
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.05
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.4
      pick: 0.17
      fit: 0.61
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.19
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.68
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 0.35
      fit: 0.77
    Avatar's Parashu:
      total: 0.62
      efficiency: 0.45
      win: 0.8
      pick: 0.41
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Hydra's Lament
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Death
    Metal, Soul Gem, Lernaean Bow, The Reaper, Gluttonous Grimoire, Tekko-Kagi, Golden
    Blade, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard, Spear of
    Desolation, Dominance, Bracer of The Abyss, Qin''s Blade, Titan''s Bane, Deathbringer,
    Demon Blade, Doom Orb, The World Stone, Ancient Signet, Sun Beam Bow, Blood-Bound
    Book, Transcendence, Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords,
    Runeforged Hammer, Berserker''s Shield, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.67
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.55
      pick: 0.37
      fit: 0.27
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.57
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.8
      pick: 0.41
      fit: 0.27
  community_ordered:
  - Hydra's Lament
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Spear of Desolation
  - Rod of Tahuti
  - Avatar's Parashu
  flex_slots:
  - Arondight
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Silverbranch
    Bow, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean Bow, Pendulum Blade, Tekko-Kagi,
    Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss, Totem of Death, Doom
    Orb, Riptalon, Golden Blade, The World Stone, Ancient Signet, Titan''s Bane, The
    Reaper, Breastplate of Valor, Dreamer''s Idol, Toxic Blade, Deathbringer, Dominance,
    Genji''s Guard, Qin''s Blade, Transcendence, Musashi''s Dual Swords, Runeforged
    Hammer, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.4
      pick: 0.17
      fit: 0.59
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.55
      pick: 0.37
      fit: 0.55
    Arondight:
      total: 0.52
      efficiency: 0.5
      win: 0.6
      pick: 0.23
      fit: 0.45
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.24
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.41
      fit: 0.24
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
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
    Underrated for this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Riptalon, Spear of Desolation, Titan''s Bane, Dominance, Obsidian Shard, Deathbringer,
    Soul Gem, The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Doom Orb, Pendulum Blade, Transcendence, The
    World Stone, Qin''s Blade, Runeforged Hammer, Dreamer''s Idol, Damaru, Rage, Ancient
    Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.4
      pick: 0.17
      fit: 0.49
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.73
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
